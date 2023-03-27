import requests
from datetime import date

def token_vk():
    with open("token_vk.txt", "rb") as tv:
        token = tv.read()
        return token


class Vktok_yadisc():
    def __init__(self, token=token_vk(),
                 vk_id=int(input("Введите свой id ВК: ")),
                 ya_tok=input("Введите токен Яндекс диска: ")):
        self.params = {"access_token": token,
                          "v": "5.131",
                          "extended": 1,
                          "album_id": "profile",
                          "owner_id": vk_id}
        self.ya_headers = {"Content-Type": "application/json",
                        "Authorization": f"OAuth {ya_tok}"}

    def Yadisk_data(self):
        ya_link = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': f"{str(date.today())}"}
        response = requests.put(ya_link, headers=self.ya_headers, params=params)

    def ya_up(self):
        self.Yadisk_data()
        ya_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        vk_url = "https://api.vk.com/method/photos.get"
        resp = requests.get(vk_url, params=self.params)
        for i in resp.json()["response"]["items"]:
            for s in i["sizes"]:
                files_path = f"{date.today()}/{i['date']}.jpg"
                params = {"path": files_path, "url": s["url"]}
                if s["type"] == "z":
                    response = requests.post(ya_url, headers=self.params, params=params)


