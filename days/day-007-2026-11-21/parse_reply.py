import requests

# 第 7 天 · 把回答拆开用：只取正文、处理报错
# 在第 6 天 call_api.py 的基础上加两层保护：
# 一是用 .get() 取回答，缺东西也不崩；二是用 try/except 接住连不上、回的不是 json 的情况。

BASE_URL = "https://api.helloltq.dpdns.org/v1"
MODEL = "deepseek-v4.1-flash-1017"


def get_reply(data):
    """从大模型回来的字典里只取正文；取不到就回 None，绝不报错。"""
    if not isinstance(data, dict):
        return None
    choices = data.get("choices") or []
    if not choices:
        return None
    first = choices[0]
    if not isinstance(first, dict):
        return None
    message = first.get("message") or {}
    content = message.get("content")
    if not isinstance(content, str):
        return None
    content = content.strip()
    if not content:
        return None
    return content


def ask(api_key, question):
    """发一句话，回来只给正文；出问题就把原因印出来，回 None。"""
    try:
        r = requests.post(
            BASE_URL + "/chat/completions",
            headers={
                "Authorization": "Bearer " + api_key,
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": question}],
                "max_tokens": 200,
            },
            timeout=60,
        )
    except requests.exceptions.RequestException as e:
        print("没连上服务器：", e)
        return None

    print("状态码：", r.status_code)
    if r.status_code != 200:
        print("这次没调通，服务器回的是：")
        print(r.text)
        return None

    try:
        data = r.json()
    except ValueError:
        print("服务器回的不是 json，没法拆：")
        print(r.text)
        return None

    return get_reply(data)


# 密钥不在文件里写死：跑起来之后粘贴，用完就忘，不留痕迹。
api_key = input("把你的令牌粘贴进来（粘贴后按回车，不会显示在文件里）：").strip()
question = input("想问大模型什么？直接打一句话：").strip()

reply = ask(api_key, question)
if reply is None:
    print("这次没拿到正文，上面已经印了原因，改好再跑一次就行。")
else:
    print("大模型回你：")
    print(reply)
