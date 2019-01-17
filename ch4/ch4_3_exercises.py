print("4-3:")
for v in range(1, 21):
    print(v)

print("\n")
print("4-5:")
list4_5 = list(range(1, 1000001))
print(min(list4_5))
print(max(list4_5))
print(sum(list4_5))

print("\n")
print("4-6:")
list4_6 = list(range(1, 21, 2))
for v in list4_6:
    print(v)

print("\n 4-7:")
for v in list(range(3, 30, 3)):
    print(v)

print("\n 4-8:")
list4_8 = []
for v in range(1, 11):
    list4_8.append(v**3)
print(list4_8)

print("\n 4-9:")
list4_9 = [v ** 3 for v in range(1, 11)]
for v in list4_9:
    print(v)

print(list4_9)