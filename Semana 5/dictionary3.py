list_of_keys = ['height','college','country']
player = {
    'name':'Stephen Curry', 
    'height':'1.88 m', 
    'country':'USA',
    'current_team':'Golden State',
    'position':'Point Guard',
    'debut':'October 2009',
    'college':'Davidson'
    }

print(f'NBA player data: {player}')

for element in list_of_keys:
    player.pop(element)

print(f'NBA player data (updated): {player}')