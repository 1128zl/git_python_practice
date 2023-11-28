from pathlib import Path
from datetime import datetime 
import csv
import matplotlib.pyplot as plt
import pytest


def visualize_temperature_data(file_path):
    lines = file_path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
        try:
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print("Missing data for {current_time}")
        else:
            lows.append(low) 
            highs.append(high)
            dates.append(current_date)
    
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

    ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley", fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature(F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()


# 测试函数
def test_visualize_temperature_data():
    # 已存在文件的数据可视化测试
    existing_file_path = Path('death_valley_2021_full.csv')
    visualize_temperature_data(existing_file_path)

    # 未存在文件的数据可视化测试
    non_existing_file_path = Path('death_valley_2022_full.csv')
    with pytest.raises(FileNotFoundError):
        visualize_temperature_data(non_existing_file_path)


# 执行测试
test_visualize_temperature_data()
