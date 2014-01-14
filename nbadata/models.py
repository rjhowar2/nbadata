from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team_abbreviation = models.CharField(max_length=6)
    gp = models.IntegerField(max_length=4, null=True)
    min = models.FloatField(null=True)
   
class ReboundData(models.Model):
    player = models.ForeignKey(Player)
    reb = models.FloatField(null=True)
    reb_chance = models.FloatField(null=True)
    reb_col_pct = models.FloatField(null=True)
    reb_contested = models.FloatField(null=True)
    reb_uncontested = models.FloatField(null=True)
    reb_uncontested_pct = models.FloatField(null=True)
    reb_tot = models.IntegerField(max_length=6, null=True)
    oreb = models.FloatField(null=True)
    oreb_chance = models.FloatField(null=True)
    oreb_col_pct = models.FloatField(null=True)
    oreb_contested = models.FloatField(null=True)
    oreb_uncontested = models.FloatField(null=True)
    oreb_uncontested_pct = models.FloatField(null=True)
    dreb = models.FloatField(null=True)
    dreb_chance = models.FloatField(null=True)
    dreb_col_pct = models.FloatField(null=True)
    dreb_contested = models.FloatField(null=True)
    dreb_uncontested = models.FloatField(null=True)
    dreb_uncontested_pct = models.FloatField(null=True)
    
class DefenseData(models.Model):
    player = models.ForeignKey(Player)
    blk = models.FloatField(null=True)
    stl = models.FloatField(null=True)
    fgm_defend_rim = models.FloatField(null=True)
    fga_defend_rim = models.FloatField(null=True)
    fgp_defend_rim = models.FloatField(null=True)
    blk_tot = models.IntegerField(max_length=6, null=True)

class PassingData(models.Model):
    player = models.ForeignKey(Player)
    passing = models.FloatField(null=True) 
    ast = models.FloatField(null=True)
    ast_ft = models.FloatField(null=True)
    ast_sec = models.FloatField(null=True)
    ast_pot = models.FloatField(null=True)
    pts_crt = models.FloatField(null=True)
    pts_crt_48 = models.FloatField(null=True)
    ast_tot = models.IntegerField(max_length=6, null=True)
    
class PullupData(models.Model):
    player = models.ForeignKey(Player)
    pts = models.FloatField(null=True)
    fgm = models.FloatField(null=True)
    fga = models.FloatField(null=True)
    fg_pct = models.FloatField(null=True)
    fg3m = models.FloatField(null=True)
    fg3a = models.FloatField(null=True)
    fg3_pct = models.FloatField(null=True)
    efg_pct = models.FloatField(null=True)
    pts_tot = models.IntegerField(max_length=6, null=True)

class DriveData(models.Model):
    player = models.ForeignKey(Player)
    dvs = models.FloatField(null=True)
    dpp = models.FloatField(null=True)
    dtp = models.FloatField(null=True)
    fg_pct = models.FloatField(null=True)
    pts_48 = models.FloatField(null=True)
    dpp_tot = models.IntegerField(max_length=6, null=True)
    dvs_tot = models.IntegerField(max_length=6, null=True)

class CatchshootData(models.Model):
    player = models.ForeignKey(Player)
    pts = models.FloatField(null=True)
    fgm = models.FloatField(null=True)
    fga = models.FloatField(null=True)
    fg_pct = models.FloatField(null=True)
    fg3m = models.FloatField(null=True)
    fg3a = models.FloatField(null=True)
    fg3_pct = models.FloatField(null=True)
    efg_pct = models.FloatField(null=True)
    pts_tot = models.IntegerField(max_length=6, null=True)

class ShootingData(models.Model):
    player = models.ForeignKey(Player)
    pts = models.FloatField(null=True)
    pts_drive = models.FloatField(null=True)
    fgp_drive = models.FloatField(null=True)
    pts_close = models.FloatField(null=True)
    fgp_close = models.FloatField(null=True)
    pts_catch_shoot = models.FloatField(null=True)
    fgp_catch_shoot = models.FloatField(null=True)
    pts_pull_up = models.FloatField(null=True)
    fgp_pull_up = models.FloatField(null=True)
    fga_drive = models.FloatField(null=True)
    fga_close = models.FloatField(null=True)
    fga_catch_shoot = models.FloatField(null=True)
    fga_pull_up = models.FloatField(null=True)
    efg_pct = models.FloatField(null=True)


    