snake = 'python_base_practice'
pascal = snake.replace('_',' ').title().replace(" ",'')
#print(pascal) #PythonBasePractice

def conversion(snake):
    res = []
    a = snake.split('_')
    for i in a:
        i = i.title()
        res.append(i)
    res = ''.join(res)
    return res
output = conversion(snake)
print(output)
