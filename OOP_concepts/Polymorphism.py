class nepal:
    def country(self):
        print('This is Nepal.')
    def lang(self):
        print('Nepalese language is the national language.')
    def cond(self):
        print('It is a developing country.')

class USA:
    def country(self):
        print('This is USA.')
    def lang(self):
        print("English is the native language.")
    def cond(self):
        print('USA is a developed country.')

n1 = nepal()
u1 = USA()

for obj in (n1, u1):
    obj.country()
    obj.lang()
    obj.cond()