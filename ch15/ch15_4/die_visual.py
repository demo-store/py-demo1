import pygal

from die import Die

# 创建一个D6
die61 = Die()
die62 = Die()

results = []
for roll_num in range(1000):
    result = die61.roll() + die62.roll()
    results.append(result)

# 分析结果
frequencies = []
size = die61.num_sides + die62.num_sides
for value in range(2, size + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file("die_visual_d2.svg")

