from collections import OrderedDict

dic = OrderedDict([('Inez',22), ('Jihyaa',24)]) #OrderedDict({'Inez': 22, 'Jihyaa': 24})
dic.update({'Cairo':5})
dic.move_to_end('Cairo', last=False)
print(str(dic))

  