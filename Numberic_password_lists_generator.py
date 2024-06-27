from time import *

def intro():
    print("")
    print("WELCOME TO P@CR7".center(100, "_"))
    print("")
    print("P@CR7 is generat a numberic password lists.".center(100, "~"))
    print("start with 2 digits, end with 9 digits.".center(100, "~"))
    print("")
    print("DEVELOPED BY ^HXBNO^".center(100))
    print("".center(100, "_"))
    sleep(3)
    print("")

def body():
    global inp
    inp = input("Enter a digit (2 - 9)\n>> ")
    print("\n")
    print("Please Wait...")
    print("\n")
    sleep(2)

def body2():
    if inp == "2":
        p2()
    elif inp == "3":
        p3()
    elif inp == "4":
        p4()
    elif inp == "5":
        p5()
    elif inp == "6":
        p6()
    elif inp == "7":
        p7()
    elif inp == "8":
        p8()
    elif inp == "9":
        p9()
    else:
        print("Something is wrong")

def p2():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            print(a, b)

def p3():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            c = -1
            while c < 9:
                c += 1 
                print(a, b, c)

def p4():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            c = -1
            while c < 9:
                c += 1
                d = -1
                while d < 9:
                    d += 1 
                    print(a, b, c, d)

def p5():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            c = -1
            while c < 9:
                c += 1
                d = -1
                while d < 9:
                    d += 1 
                    e = -1
                    while e < 9:
                        e += 1
                        print(a, b, c, d, e)

def p6():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            c = -1
            while c < 9:
                c += 1
                d = -1
                while d < 9:
                    d += 1 
                    e = -1
                    while e < 9:
                        e += 1
                        f = -1
                        while f < 9:
                            f += 1
                            print(a, b, c, d, e, f)

def p7():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            c = -1
            while c < 9:
                c += 1
                d = -1
                while d < 9:
                    d += 1 
                    e = -1
                    while e < 9:
                        e += 1
                        f = -1
                        while f < 9:
                            f += 1
                            g = -1
                            while g < 9:
                                g += 1
                                print(a, b, c, d, e, f, g)

def p8():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            c = -1
            while c < 9:
                c += 1
                d = -1
                while d < 9:
                    d += 1 
                    e = -1
                    while e < 9:
                        e += 1
                        f = -1
                        while f < 9:
                            f += 1
                            g = -1
                            while g < 9:
                                g += 1
                                h = -1
                                while h < 9:
                                    h += 1
                                    print(a, b, c, d, e, f, g, h)

def p9():
    a = -1
    while a < 9:
        a += 1
        b = -1
        while b < 9:
            b += 1
            c = -1
            while c < 9:
                c += 1
                d = -1
                while d < 9:
                    d += 1 
                    e = -1
                    while e < 9:
                        e += 1
                        f = -1
                        while f < 9:
                            f += 1
                            g = -1
                            while g < 9:
                                g += 1
                                h = -1
                                while h < 9:
                                    h += 1
                                    i = -1
                                    while i < 9:
                                        i += 1
                                        print(a, b, c, d, e, f, g, h, i)

def end():
    print("\n")
    print(" Thank you from using this tool. ".center(100, "$"))
    print("Developed in 6/27/2024".center(100))
    print("\n")



intro()
body()
body2()
end()