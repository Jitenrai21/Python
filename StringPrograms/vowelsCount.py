def vowels(string):
    string = string.lower()
    lst = [char for char in string if char in 'aeiou']
    if lst:
        dict, lst1 = {}, []
        for char in lst:
            dict['a'] = lst.count('a')
            dict['e'] = lst.count('e')
            dict['i'] = lst.count('i')
            dict['o'] = lst.count('o')
            dict['u'] = lst.count('u')
        for i,j in dict.items():
            if j == 0:
                lst1.append(i)
        if lst1:
            print(f"Vowels letters are present except for {','.join(lst1)}.")
        else:
            print('All vowels are present.')
    else:
        print('No vowels present!')

vowels('Inezwa')
                
                            