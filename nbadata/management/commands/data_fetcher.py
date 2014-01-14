from nbadata.models import Player, PullupData, DriveData, DefenseData, PassingData, ReboundData, CatchshootData, ShootingData
from django.core.management.base import BaseCommand, CommandError
import urllib2
import json

ADDRESS_LIST = [
     {'model': PullupData ,'url': "http://stats.nba.com/js/data/sportvu/pullUpShootData.js"}, 
     {'model': DriveData,'url': "http://stats.nba.com/js/data/sportvu/drivesData.js"}, 
     {'model': DefenseData,'url': "http://stats.nba.com/js/data/sportvu/defenseData.js"}, 
     {'model': PassingData,'url': "http://stats.nba.com/js/data/sportvu/passingData.js"}, 
     {'model': ReboundData,'url': "http://stats.nba.com/js/data/sportvu/reboundingData.js"}, 
     {'model': CatchshootData,'url': "http://stats.nba.com/js/data/sportvu/catchShootData.js"}, 
     {'model': ShootingData,'url': "http://stats.nba.com/js/data/sportvu/shootingData.js"}
]

#Player data is included in each feed
PLAYER_KEYS = ["first_name","last_name","team_abbreviation","gp","min"]
IGNORE_KEYS = ["player_id", "player"]


class Command(BaseCommand):
    option_list = BaseCommand.option_list
    help = 'Management command to get data from stats.nba.com'

    def handle(self, **options):
         fetch_data()

def fetch_data():
    for address in ADDRESS_LIST:
        raw_data = _get_data_dict(address['url'])
        
        #Map the data to the correct headers, pass is reserved catch it here
        keys = map(lambda x:'passing' if x == 'PASS' else x.lower(),raw_data['headers'])
        values = raw_data['rowSet']
        stats = [dict(zip(keys,value)) for value in values]
        
        for s in stats:
            _save_to_model(address['model'], s)

def _save_to_model(model, data):
        p_id = int(data['player_id']) 
        
        #save the player data first
        Player.objects.get_or_create(pk=data['player_id'])
        kwargs = {}
        for key in PLAYER_KEYS:
            kwargs[key] = data[key]
        Player(**kwargs)
        Player.save()
        
        model.objects.get_or_create(player_id=p_id)
        kwargs = {}
        for key, value in data.iteritems():
            if key not in PLAYER_KEYS and key not in IGNORE_KEYS:
                kwargs[key] = value
        
        model(**kwargs)
        model.save()
        
        

def _get_data_dict(url):
    """
        gets the response html and returns the usable data as a dict
    """
    response = urllib2.urlopen(url)
    rsp_str = response.read()
    
    #rsp_str is in the form "var foo = {...};"
    json_str = '{' + rsp_str.split('{', 1)[1][:-1]

    return json.loads(json_str)['resultSets'][0]