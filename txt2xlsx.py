#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
from openpyxl import Workbook

# 将文件夹下（不包括子文件夹）的文件转换为xlsx


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
                        # print(type(item))
                        # 如果是有下滑线的字符串，不直接转浮点数，防止发生1_2_3这种转化为123
                        # 数值转为浮点数，防止字符串格式的数值在excel中显示有一个小绿点
                        if '_' not in item:
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
