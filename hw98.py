


def swapdata():

    filename1= input("enter a file name")
    filename2=input("enter another file name")

    with open(filename1,'r') as a:
        data_a = a.read()


    with open(filename2,'r') as b:
        data_b = b.read()

    with open(filename1,'w') as a:
        a.write(data_b)

    with open(filename2,'w') as b:
        b.write(data_a)

swapdata()