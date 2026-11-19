import requests

# 第 6 天 · 亲手调通一次大模型 API
# 只用 Day 4 学过的 requests，不装新东西。

BASE_URL = "https://api.helloltq.dpdns.org/v1"
MODEL = "deepseek-v4.1-flash-1017"

# 密钥不在文件里写死：跑起来之后粘贴，用完就忘，不留痕迹。
# 令牌在你自己的中转后台“令牌”里新建、复制；它像密码一样，别发给别人，也别写进要上传的文件。
api_key = input("把你的令牌粘贴进来（粘贴后按回车，不会显示在文件里）：").strip()
question = input("想问大模型什么？直接打一句话：").strip()

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

print("状态码：", r.status_code)
if r.status_code != 200:
    print("这次没调通，服务器回的是：")
    print(r.text)
else:
    data = r.json()
    reply = data["choices"][0]["message"]["content"]
    print("大模型回你：")
    print(reply)
