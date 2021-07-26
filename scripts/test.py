import os, sys
import json

#os.chdir(sys.path[0])

"""
with open('./data/weibo_all.json') as f:
    for line in f:
        data = json.loads(line)
        print(data)
        break
    """

data = [json.loads(line.strip()) for line in open('./data/weibo_dev.json')]

print(data)
print(len(data))
