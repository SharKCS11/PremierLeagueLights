import os
from time import sleep
import requests
import json
from dotenv import load_dotenv


load_dotenv(verbose=True)
#print (os.getenv("LIFX_AUTH")) # Get key.

colors = {}
time_multiplier = 1.5
# hue, sat, brightness, delay states.
# Total 1500ms
'''
Colors:
    Liverpool - Red
    Tottenham - White + dark blue
    Man City - Light blue
    Chelsea - Deep blue + white
    Arsenal - White + red
    Man Utd - Red + Yellow/orange
    Leicester - White + blue + white
    Wolves - Orange
    Watford - Yellow
    Everton - Blue
    West Ham - Burgundy
    Bournemouth - Dark red + black.
    Brighton & Hove - Blue + pink
    Crystal Palace - Blue + red + blue + red
    Newcastle United FC - White + black + white + black
    Cardiff - Blue + black + red
    Southampton - Red + white + red
    Burnley - Sky Blue + dark red + sky blue
    Fulham - White + black
    Huddersfield - Dark blue + light blue + dark blue + light blue
'''
def getWhite(delay_in):
    return [150, 0, 0.9, delay_in]

def getBlack(delay_in):
    return [0, 1, 0.01, delay_in]

colors["Liverpool FC"] = [ [352, 1, 0.9, 1000] ]
colors["Tottenham Hotspur FC"] = [ [150, 0, 0.9, 500], [243, 0.95, 0.24, 500] ]
colors["Mancheseter City FC"] = [ [194, 0.72, 0.90, 1000] ]
colors["Chelsea FC"] = [ [236, 1, 0.49, 500], [150, 0, 0.9, 500] ]
colors["Arsenal FC"] = [ [150, 0, 0.9, 500] , [349, 0.75, 0.81, 500] ]
colors["Manchester United FC"] = [ [359, 1, 0.85, 500], [37, 1, 0.85, 500] ]
colors["Leicester City FC"] = [ [215, 1, 0.86, 400], getWhite(200), [215, 1, 0.86, 400]]
colors["Wolverhampton Wanderers FC"] = [ [36.6, 1, 0.55, 1000] ]
colors["Watford FC"] = [ [53.4, 1, 0.55, 1000] ]
colors["Everton FC"] = [[244.6, 1, 0.55, 1000]]
colors["West Ham United FC"] = [[330.4, 1, 0.2, 1000]]
colors["AFC Bournemouth"] = [ [14, 1, 0.3, 333], getBlack(334), [14, 1, 0.3, 333] ] 
colors["Brighton & Hove Albion FC"] = [ [220.7, 0.70, 0.86, 500], [300, 0.43, 0.86, 500] ]
colors["Crystal Palace FC"] = [ [252, 1, 0.47, 250], [350, 1, 0.47, 250],[252, 1, 0.47, 250], [350, 1, 0.47, 250] ]
colors["Newcastle United FC"] = [getWhite(250), getBlack(250), getWhite(250), getBlack(250)]
colors["Cardiff City FC"] = [[252, 1, 0.47, 300], getBlack(400), [354, 1, 0.6, 300]]
colors["Southampton FC"] = [ [354, 1, 0.6, 300], getWhite(400), [354, 1, 0.6, 300] ]
colors["Burnley FC"] = [ [188, 1, 0.85, 400], [2, 1, 0.4, 200], [188, 1, 0.85, 400] ]
colors["Fulham FC"] = [getWhite(600), getBlack(400)]
colors["Huddersfield Town AFC"] = [ [248, 1, 0.38, 250], [194, 0.72, 0.77, 250], [248, 1, 0.38, 250], [194, 0.72, 0.77, 250] ]

lifx_url = "https://api.lifx.com/v1/lights/id:%s/state" %(os.getenv("LIFX_ID"))
print (lifx_url)

# Make requests.
def set_color(col_string):
    headers = {'Authorization':os.getenv('LIFX_AUTH'), 'Content-Type':'application/json'}
    json_data = {"color": col_string, "duration": "0.01", "fast":True}
    r = requests.put(lifx_url, data=json.dumps(json_data), headers=headers);
    print (r)

def set_off():
    col_string = "hue:0 saturation:0 brightness:0.01"
    set_color(col_string)
    sleep(2.5)

def set_light_and_delay(cline):
    c_hue = cline[0]
    c_sat = cline[1]
    c_bri = cline[2]
    c_delay = cline[3]
    col_string = "hue:%.1f saturation:%.2f brightness:%.2f" %(c_hue, c_sat, c_bri)
    print (col_string)
    set_color(col_string)
    sleep(c_delay*time_multiplier/1000)

teams = ["Liverpool FC", "Manchester United FC", "Crystal Palace FC", "Huddersfield Town AFC"]
set_off()
for team in teams:
    loc_colors = colors[team];
    for cline in loc_colors:
        set_light_and_delay(cline);
    set_off()

    
