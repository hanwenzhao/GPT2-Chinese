import os, sys
import docx2txt
import json

def find_all_file(folder_path):
    file_path = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path.append(os.path.join(root, filename))
    
    return file_path



if __name__ == "__main__":
    os.chdir(sys.path[0])

    file_path = find_all_file('./data/data_0813')

    with open('./data/data_0813.json', 'w') as out_file:
        for file in file_path:
            print(file)
            text = docx2txt.process(file)
            for line in text.splitlines():
                if line != "":
                    tmp = {'text': line.strip()}
                    #print(line.strip())
                    json.dump(tmp, out_file)
                    out_file.write('\n')
            

