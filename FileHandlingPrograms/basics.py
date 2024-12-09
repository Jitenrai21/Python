with open('E:\github_clones\Python\FileHandlingPrograms\demo.txt', 'r') as file:
    # for line in file:
    #     for word in line.split():
    #         print(word)
    while 1:
        char = file.read(1)
        if not char: 
            break
        print(char)
    file.close()

