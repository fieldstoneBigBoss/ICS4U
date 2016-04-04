def question():
    a=input("what's your number\\")
    return float(a)
question()



def price():
    b=input("please input a number.")


def ex3(x):
    print("$",round(x,2),sep="")

print(ex3(5.1135450987534567))


def encode(x):
    y=""
    for i in range(len(x)):
        y=y+chr(ord(x[i])+1)
    return y


def decode(x):
    y=""
    for i in range(len(x)):
        y=y+chr(ord(x[i])-1)
    return y

print(encode("bob"))
print(decode("nihao"))

