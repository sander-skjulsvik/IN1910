a0 = 0

def fun1():

    a1 = 1.0
    print(a0)

    def fun21():
        a21 = 2
        print(a0)
        print(a1)
    # print(a21) # does not work
    fun21()

if __name__ == "__main__":
    fun1()