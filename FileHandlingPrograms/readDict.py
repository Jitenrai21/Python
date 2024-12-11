import pickle

try:
    file = open(r'E:\github_clones\Python\FileHandlingPrograms\dic.txt','rb')
    dict_lines = pickle.load(file)
    for line in dict_lines:
        print(line)
    file.close()
except Exception as e:
    print(f'Error: {e}')