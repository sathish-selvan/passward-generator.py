import random ,string

def create_passward(lenght,num=False,strenght="weak"):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letters = lower+upper
    dig = string.digits
    punct = string.punctuation
    pwd = ""
    if strenght == "weak":
        if num:
            lenght -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(lenght):
            pwd += random.choice(lower)

    elif strenght == "strong":
        if num:
            lenght -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(lenght):
            pwd += random.choice(letters)

    elif strenght == "very":
        ran = random.randint(2,4)
        if num:
            lenght = lenght - ran
            for i in range(ran):
                pwd += random.choice(dig)
        lenght -= ran
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(lenght):
            pwd += random.choice(letters)

    pwd = list(pwd)
    random.shuffle(pwd)
    return ("".join(pwd))

 
print(create_passward(5,True,"weak"))