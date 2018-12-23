#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os


path="/home/shiyanlou/files"
result = []
files = os.listdir(path)
for file in files:
    json_file=path+'/'+file
    with open(json_file,'r') as f:
        s=json.load(f)
        result.append(s)
print(result)

