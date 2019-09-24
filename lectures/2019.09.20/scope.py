pi = 3.14
r = 10


def pancake_area():
    global r
    r = 15
    return pi*r**2


if __name__ == "__main__":

    print("befor calling pancake area: ", r)
    print(pancake_area())
    print("Before calling pancake area: ", r)
