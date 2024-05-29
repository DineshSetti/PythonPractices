def Demo(**data):
    for k,v in data.items():
        if k=='name' or k=='lname':
            print(k,'  : ',v)
        elif k=='age':
            print(k,'   : ',v)
        else:
            print(k,' : ',v)
Demo(name='dinesh',age=22,color='black')



