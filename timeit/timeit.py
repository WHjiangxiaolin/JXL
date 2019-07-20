import time

result = 0
start = time.time()
for i in range(1, 100000001):
    result += i
end = time.time()

print(result)
print(end - start)  #计算计算机从1加到一亿需要的时间