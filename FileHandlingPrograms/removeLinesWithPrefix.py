file1 = open(r'E:\github_clones\Python\FileHandlingPrograms\demo.txt', 'r')
file2 = open(r'E:\github_clones\Python\FileHandlingPrograms\updatedDemo.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Jihyaa')):
        print(line)

        file2.write(line)

file2.close()
file1.close()