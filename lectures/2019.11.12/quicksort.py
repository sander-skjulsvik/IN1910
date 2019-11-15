def quicksort(data):
    """Return a copy of data sorted in increasing order."""
    sdata = data[:]
    qsort(sdata, 0, len(data))
    return sdata


def qsort(data, low, high):
    """Recursively sort data[low:high] in place."""
    if high - low < 2:
        # Single or no element, no sorting needed
        return

    pivot = partition(data, low, high)
    qsort(data, low, pivot)
    qsort(data, pivot + 1, high)


def partition(data, low, high):
    """Partition data[low:high]"""
    pivot = data[high - 1]
    i = low - 1
    for j in range(low, high - 1):
        if data[j] < pivot:
            if i != j:
                i = i + 1
                data[i], data[j] = data[j], data[i]
    i += 1
    data[i], data[high - 1] = data[high - 1], data[i]
    return i


if __name__ == "__main__":
    x = [1, 8, 7, 6, 4, 3, 9, 3, 10, 5, 2]
    print("Unsorted: ", x)
    print("Sorted: ", quicksort(x))
