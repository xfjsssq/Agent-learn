# file_io.py — 第 3 天练习：文件读写，让程序记住东西
# 跑法：先 cd 到这个文件所在的文件夹，再执行 python file_io.py
# 它会在当前文件夹里生成 notes.txt 和 scores.json，读出来、改一个分数、再存回去。
# 动手改一改：把 data["小明"] = 88 改成别的分数，再跑一遍，对比 scores.json 前后有什么变化。
import json

# 1. 写一个纯文本文件：记下今天学了什么
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("第 3 天：文件读写\n")
    f.write("今天学会了 open、read、write，还有 json 的 load 和 dump。\n")

# 2. 读回来，看看写进去没有
with open("notes.txt", "r", encoding="utf-8") as f:
    print("--- notes.txt 里现在是 ---")
    print(f.read())

# 3. 写一个 JSON 文件：存三个人的分数（字典，像个小表格）
scores = {"小肥鱼": 92, "小明": 78, "小红": 85}
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, ensure_ascii=False, indent=2)

# 4. 读回来，改一个分数，再存回去
with open("scores.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print("--- 改之前 ---")
print(data)

data["小明"] = 88  # 只改一个值，别的不动

with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("scores.json", "r", encoding="utf-8") as f:
    print("--- 改之后 ---")
    print(json.load(f))
