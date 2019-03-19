from die import Die

# 创建一个D6
die6 = Die()

results = []
for roll_num in range(10):
    result = die6.roll()
    results.append(result)

print(results)
