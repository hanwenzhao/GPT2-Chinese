import os, sys
import json

def read_json_file(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))

    return data

def find_all_file(folder_path):
    file_path = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path.append(os.path.join(root, filename))
    
    return file_path


if __name__ == '__main__':
    # change current directory
    os.chdir(sys.path[0])
    # walk through all the file
    file_path = find_all_file("./data/wiki_zh")
    # load all json files into one
    data =[]
    for file in file_path:
        data.extend(read_json_file(file))
    # clip data for dev
    #data = data[:int(len(data)/1000)]
    with open('./data/weibo_all.json', 'w') as f:
        #print(f"\n Saving {len(data)} json into file ...\n")
        for json_line in data:
            json.dump(json_line, f)
            f.write('\n')
    
    