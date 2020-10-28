#! /usr/local/bin/python3
# coding:utf-8
# 批量解压，并删除压缩包
import zipfile
import os


def read_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files, dirs, root


def unzip(files, dirs, root):
    for file_name in files:
        if file_name.endswith('.zip'):
            file_zip = zipfile.ZipFile(os.path.join(root, file_name), 'r')
            file_zip.extractall(root)
            file_zip.close()
            os.remove(os.path.join(root, file_name))

    for jj in dirs:
        fis, dis, ros = read_file_name(root + "\\" + jj)
        unzip(fis, dis, ros)


if __name__ == "__main__":
    # file_path是需要解压的所有压缩包的路径
    file_path = r'C:\Users\asus\Desktop\1'
    fi, di, ro = read_file_name(file_path)
    unzip(fi, di, ro)
