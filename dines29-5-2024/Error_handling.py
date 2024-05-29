try:
    print("hello world")
except:
    print("error")
else:
    print("no error")
finally:
    print("always")


#error
try:
    print(b)
except:
    print("error")
else:
    print("no error")
finally:
    print("always")

#type error
try:
    print("abc"+12)
except TypeError:
    print("There is an type error")
except ValueError:
    print("There is an value error")
else:
    print("no error")
finally:
    print("always")