#frequency counter
string = 'This is an example. And this will give the example result for frequency counting.'
string = string.lower()
res = {key : string.count(key) for key in string.split()}
print(res)