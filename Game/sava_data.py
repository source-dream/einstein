#!python
# -*-coding:utf-8 -*-
'''
@File    :   sava_data.py
@Time    :   2023/07/10 11:33:05
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import csv
import shutil
import os

def save_rate(role1, role2, winner):
    rows = []

    with open('Data\TrianData\win_rate.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    flag = False

    for r in rows:
        if r[0].strip() == role1 and r[1].strip() == role2:
            flag = True
            if winner:
                r[2] = str(int(r[2].strip()) + 1).ljust(10)
                r[4] = "{:.6f}".format(float(r[2].strip())/(float(r[2].strip())+float(r[3].strip()))).ljust(10)
            else:
                r[3] = str(int(r[3].strip()) + 1).ljust(10)
                r[4] = "{:.6f}".format(float(r[2].strip())/(float(r[2].strip())+float(r[3].strip()))).ljust(10)

    if not flag:
        if winner:
            t = [role1.ljust(10), role2.ljust(10), '1'.ljust(10), '0'.ljust(10), '1'.ljust(10)]
        else:
            t = [role1.ljust(10), role2.ljust(10), '0'.ljust(10), '1'.ljust(10), '0'.ljust(10)]
        rows.append(t)

    with open('win_rate_updated.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    shutil.move('win_rate_updated.csv', 'Data\TrianData\win_rate.csv')