import os
from datetime import datetime, timedelta
print ('请输入开始和结束日期以及车牌号码，如果你没有输入日期，默认设置开始日期为上个月的第一天，结束日期为当前月的最后一天，查询的结果会生成一个文本文件')
# 从用户那里获取开始和结束日期
start_date_str = input("请输入开始日期（格式：YYYYMMDD）：")
end_date_str = input("请输入结束日期（格式：YYYYMMDD）：")

# 如果用户没有输入日期，设置开始日期为上个月的第一天，结束日期为当前月的最后一天
if not start_date_str:
    start_date = datetime.now().replace(day=1) - timedelta(days=1)
    start_date = start_date.replace(day=1)
else:
    start_date = datetime.strptime(start_date_str, "%Y%m%d")

if not end_date_str:
    end_date = datetime.now()
else:
    end_date = datetime.strptime(end_date_str, "%Y%m%d")

# 其他代码...
# 将字符串转换为datetime对象

def generate_file_names(start_date, end_date):
    file_names = []
    for i in range(int((end_date - start_date).days) + 1):
        day = start_date + timedelta(days=i)
        file_name = f"CameraIdentifyResults_LOG_{day.strftime('%Y%m%d')}.log"
        file_names.append(file_name)
    return file_names

def search_license_plate(license_plate, file_names):
    with open('车辆进出记录.txt', 'w', encoding='utf-8') as output_file:
        for file_name in file_names:
            file_path = os.path.join("D:\\IISpublish\\Log\\CameraIdentifyResults", file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    found = False
                    for line in f:
                        if license_plate in line:
                            output_line =  line[line.find('==') + 2:line.find('Full')].strip() + "\n"
                            output_file.write(output_line)
                            found = True
                    if not found:
                        pass
            except FileNotFoundError:        
                continue

# 从用户那里获取车牌号
license_plate = input("请输入要搜索的车牌号：")

# 生成文件名
file_names = generate_file_names(start_date, end_date)

# 搜索车牌号出现的行并显示在屏幕上
search_license_plate(license_plate, file_names)


file_names = generate_file_names(start_date, end_date)

