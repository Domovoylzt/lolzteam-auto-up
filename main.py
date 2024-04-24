import requests
import time
import json
token="Bearer "+"Ваш токен"
temisleep = 12*3600 # Вместо 12 - раз в сколько часов апать темы (зависит от ваших симп епт)
temid=[] # id ваших тем через запятую
# пример
# https://zelenka.guru/threads/6682541/
# https://zelenka.guru/threads/6837883/
# https://zelenka.guru/threads/6811950/
# temid=[6682541,6837883,6811950]
while True:
    try:
        for x in temid:

            url = "https://api.zelenka.guru/threads/"+str(x)+"/bump"

            headers = {
                "accept": "application/json",
                "authorization": token
            }
            response = requests.post(url, headers=headers)
            inf=json.loads(response.text)
            if("errors" in inf.keys()):
                print("Не удалось поднять тему",x,"Причина:",(str(inf["errors"])[2:-2]).replace("<br>\\n"," "))
            else:
                print("Успешно поднял тему с id",x)
            time.sleep(6)
        print("Прошел",len(temid),"тем. Ожидаю",temisleep//3600,"часов")
        time.sleep(temisleep)
    except Exception as err:
        print("Произошла неизвестная ошибка: ",err)
