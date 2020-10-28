#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# excel转txt
import glob
import os
import pandas as pd


def excel2txt(path):
    filelist = glob.glob(os.path.join(path, r'*.xls*'))
    for file in filelist:
        p = pd.read_excel(file, index_col=None, header=None)
        col_len = len(p.columns)
        row_len = len(p.index)
        with open(os.path.splitext(file)[0] + '.txt', 'w') as f:
            for row in range(0, row_len):
                for col in range(0, col_len):
                    content = p.iloc[row, col]
                    # pd.isnull是判断数值是否为nan的方法
                    # 如果为nan，则替换为""
                    if pd.isnull(content):
                        content = ""
                    if col == col_len - 1:
                        f.writelines(str(content).replace('\n', ''))
                        continue
                    f.writelines(str(content))
                    f.writelines('\t')
                f.writelines('\n')


if __name__ == "__main__":
    filedir = r'C:\Users\asus\Desktop\1\test'
    excel2txt(filedir)
