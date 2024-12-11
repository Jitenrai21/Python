def removeDup(input_file, output_file):
    seen = set()
    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as in_file:
            for line in in_file:
                if line not in seen:
                    out_file.write(line)
                    seen.add(line)
input_file = r'E:\github_clones\Python\FileHandlingPrograms\demo.txt'
output_file = r'E:\github_clones\Python\FileHandlingPrograms\setDemo.txt'
removeDup(input_file, output_file)

