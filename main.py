import requests
import time
import json
token="Bearer "+"ТУТ ВАШ ТОКЕН АПИ"
temisleep = 12*3600 # Вместо 12 - раз в сколько часов апать темы (зависит от ваших симп епт)
temid=[] # id ваших тем через запятую
# пример
# https://zelenka.guru/threads/6682541/
# https://zelenka.guru/threads/6837883/
# https://zelenka.guru/threads/6811950/
# temid=[6682541,6837883,6811950]
while True:
    for x in temid:
        url = "https://api.zelenka.guru/threads/"+str(x)+"/bump"

        headers = {
            "accept": "application/json",
            "authorization": token
        }
        response = requests.post(url, headers=headers)
        if response.status_code==200 :
            print(response.text)
            print("Успешно поднял тему с id",x)
        else:
            print("Ошибка поднятия темы с id",x)
            print(str(json.loads(response.text)["errors"])[2:-2])
        time.sleep(6)
    time.sleep(temisleep)
