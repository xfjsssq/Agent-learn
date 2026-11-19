import requests

print("requests 版本：", requests.__version__)

try:
    r = requests.get("https://httpbin.org/get", timeout=10)
    print("状态码：", r.status_code)
    print("拿到数据了，长度：", len(r.text))
except Exception as e:
    print("这次没连上，报错是：", e)
