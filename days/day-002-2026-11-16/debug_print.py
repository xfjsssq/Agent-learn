# debug_print.py — 第 2 天练习：用 print() 当探照灯
# 跑法：在命令行里执行 python debug_print.py
# 先看有 bug 的版本输出，再看修好并加了 print 的版本，对比两次输出哪里不一样。
# 动手改一改：把 average_buggy 里的 total = s 改成 total = total + s，再跑一遍。

def average_buggy(scores):
    total = 0
    for s in scores:
        total = s  # BUG：应该是 total = total + s，这里写成了“换成”，不是“加上”
    return total / len(scores)


def average_fixed(scores):
    total = 0
    for s in scores:
        print("这一轮 s =", s, "加之前 total =", total)
        total = total + s
        print("加之后 total =", total)
    return total / len(scores)


scores = [78, 92, 85]

print("--- 有 bug 的版本 ---")
print("平均分是", average_buggy(scores))

print("--- 修好并加了 print 的版本 ---")
print("平均分是", average_fixed(scores))
