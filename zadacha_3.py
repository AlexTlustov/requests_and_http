import requests
import json
import time

def all_quest_python(unixtime): 
    url = (f'https://api.stackexchange.com/2.3/questions?fromdate={int(unixtime) - 172800}&todate={int(unixtime)}&order=desc&sort=activity&tagged=Python&site=stackoverflow')  
    resp = requests.get(url)
    data = resp.json()
    new_list = data['items']
    final_list = []
    for obj in new_list:
        final_list.append(obj['title'])
    print('Все вопросы за послдении 2 дня:')
    print('\n'.join(final_list))
    return
    

unixtime = time.time()
all_quest_python(unixtime)

