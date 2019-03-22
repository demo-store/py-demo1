import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 对列表调用了enumerate()来获取每个元素的索引及其值。
    for index, column_header in enumerate(header_row):
        print(index, column_header)
