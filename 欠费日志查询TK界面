import tkinter as tk
from tkinter import filedialog
import re

def extract_info_from_logs(log_text):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}).*?当前时间(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}):存在待结算订单,车牌号(\w+),订单号\[(\d+)\],.*?显示的应收总金额:(\d+\.\d{2})'
    matches = re.findall(pattern, log_text)
    result = ""
    for match in matches:
        timestamp = match[0]
        current_time = match[1]
        license_plate = match[2]
        order_number = match[3]
        total_amount = match[4]
        result += f"时间: {current_time}, 车牌号码: {license_plate}, 订单号码: {order_number}, 收费金额: {total_amount}\n"
    with open('output.txt', 'w') as file:
        file.write(result)

def select_files_and_extract():
    file_paths = filedialog.askopenfilenames()
    combined_logs = ""
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:  # Specify encoding as 'utf-8' and ignore errors
            combined_logs += file.read()
    extract_info_from_logs(combined_logs)

# 创建GUI
root = tk.Tk()
root.title("江西停简单跟车逃费车辆日志提取器")
# 调整窗口大小
root.geometry("400x200")
# 添加文本内容介绍
intro_label = tk.Label(root, text="请选择要提取信息的日志文件：")
intro_label.pack()
# 创建按钮以选择文件并触发提取
select_button = tk.Button(root, text="选择文件", command=select_files_and_extract)
select_button.pack()

root.mainloop()
