try:
    print("abc")
    # raise ZeroDivisionError
    raise AttributeError
except ZeroDivisionError:
    print("There is an zero division error")
except AttributeError:
    print("There is an Attribute Error")
# except ValueError:
#     print("There is an value error")
# else:
#     print("no error")
# finally:
#     print("program runned successfully")


try:
    print("hii ")
    raise ZeroDivisionError
except ZeroDivisionError:
    print("There is an type error")
else:
    print("no error")
finally:
    print("always")