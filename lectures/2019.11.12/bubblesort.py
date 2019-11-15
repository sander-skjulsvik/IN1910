def bubblesort(data):
    """Return copy of data sorted in increasing order."""
    sdata = data[:]
    for end in reversed(range(len(sdata))):
        for i in range(end):
            if sdata[i] > sdata[i + 1]:
                sdata[i], sdata[i + 1] = sdata[i + 1], sdata[i]
    return sdata


if __name__ == "__main__":
    x = [1, 8, 7, 6, 4, 3, 9, 3, 10, 5, 2]
    print("Unsorted: ", x)
    print("Sorted: ", bubblesort(x))
