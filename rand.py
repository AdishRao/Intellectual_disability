class a:
    def __init__(self):
        print('a')
        print('b')
        i=1
        while i<10000:
            print('c')
            i+=1
        input()
    
    def ret(self):
        return 'hello'

af = a()
print(af.ret())