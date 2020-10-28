#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
from openpyxl import Workbook

# 将文件夹下（不包括子文件夹）的文件转换为xlsx
# 目前发现一个Bug，如果是由_连接的数字，中间的_会被删掉，转成纯数字


def read_filename(file_dir):
    for root, dirs, files in os.walk(file_dir):  # os.walk遍历整个文件夹
        return files, dirs, root


def txt_xlsx(files, root):
    for file in files:
        if file.endswith(".txt"):  # 只转换txt格式
            try:
                f = open(os.path.join(root, file))
                xls = Workbook()  # 创建工作簿
                sheet = xls.active
                x = 1
                while True:
                    line = f.readline()  # 逐行读入
                    if not line:  # 空行停止
                        break
                    line = line.rstrip('\n')
                    for i in range(len(line.split('\t'))):
                        item = line.split('\t')[i]
                        if item.isdigit():  # 如果是数值，转化为浮点型
                            try:
                                item = float(item)
                            except ValueError:
                                pass
                        sheet.cell(x, i+1).value = item  # x单元格经度，i+1 单元格纬度，输出内容
                    x += 1  # excel另起一行
                f.close()  # 关闭工作簿
                filename = os.path.splitext(file)  # 将文件名和后缀拆分开
                outfile = filename[0] + ".xlsx"  # 将后缀名改为xlsx
                xlsxname = os.path.join(root, outfile)
                xls.save(xlsxname)  # 保存xlsx文件
            except:
                raise


if __name__ == "__main__":
    fi, di, rt = read_filename(r"C:\Users\asus\Desktop\1\test2")
    txt_xlsx(fi, rt)
