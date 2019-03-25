import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件钟获取最高气温
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    # 设置图形的格式
    plt.title("Daily high temperatures", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

