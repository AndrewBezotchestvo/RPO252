
number = 10

# def info():
#     global number
#     number = 20
#     #print(number)
#
def info2():
    number = 20
    def info3():
        #nonlocal number
        number = 30
    info3()  # могу вызвать
    print(number)


info2()

#info3() не могу вызвать
# print(number)
