#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
import xlwt
import os

# 将文件夹及子文件夹下的所有txt转换为xls


def read_filename(file_dir):
    for root, dirs, files in os.walk(file_dir):  # os.walk遍历整个文件夹
        return files, dirs, root


def txt_xls(files, dirs, root):
    for file in files:
        if file.endswith(".txt") | file.endswith(".tsv"):  # 只转换txt格式
            try:
                f = open(os.path.join(root, file))
                xls = xlwt.Workbook()  # 创建工作簿
                sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
                x = 0
                while True:
                    line = f.readline()  # 逐行读入
                    if not line:  # 空行停止
                        break
                    line = line.rstrip('\n')
                    for i in range(len(line.split('\t'))):
                        item = line.split('\t')[i]
                        # 如果是有下滑线的字符串，不直接转浮点数，防止发生1_2_3这种转化为123
                        # 数值转为浮点数，防止字符串格式的数值在excel中显示有一个小绿点
                        if '_' not in item:
                            try:
                                item = float(item)
                            except ValueError:
                                pass
                        sheet.write(x, i, item)  # x单元格经度，i+1 单元格纬度，输出内容
                    x += 1  # excel另起一行
                f.close()  # 关闭工作簿
                filename = os.path.splitext(file)  # 将文件名和后缀拆分开
                outfile = filename[0] + ".xls"  # 将后缀名改为xls
                xlsname = os.path.join(root, outfile)
                xls.save(xlsname)  # 保存xls文件
            except:
                raise
    for dic in dirs:  # 子文件夹下的txt也转换为xls
        fi, di, ro = read_filename(root + "\\" + dic)
        txt_xls(fi, di, ro)


if __name__ == "__main__":
    fis, dis, rot = read_filename(r"C:\Users\asus\Desktop\1\test2")
    txt_xls(fis, dis, rot)
