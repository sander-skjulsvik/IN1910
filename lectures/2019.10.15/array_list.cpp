#include <exception>
#include <iostream>
using namespace std;

class ArrayList {
   public:
    int size;

   private:
    int* data;
    int capacity;

   public:
    ArrayList() {
        cout << "Calling ArrayList()" << endl;
        size = 0;
        capacity = 10000;
        data = new int[capacity];
    }
    ArrayList(int c) {
        cout << "Calling ArrayList()" << endl;
        size = 0;
        capacity = c;
        data = new int[capacity];
    }
    ArrayList(initializer_list<int> array) {
        cout << "Calling Array(initializer_list<int> array)" << endl;
        capacity = 10000;
        data = new int[capacity];
        copy(array.begin(), array.end(), data);
        size = array.size();
    }
    ~ArrayList() {
        delete[] data;
    }

    void resize() {
        capacity *= 2;
        cout << "Resizing - new capacity is " << capacity << endl;
        int* tmp = new int[capacity];
        for (int i = 0; i < size; i++) {
            tmp[i] = data[i];
        }
        delete[] data;
        data = tmp;
    }

    void append(int x) {
        if (size >= capacity) {
            resize();
        }
        data[size] = x;
        size++;
    }

    int& get(int i) {
        if ((i < size) && (i >= 0)) {
            return data[i];
        } else {
            throw out_of_range("Index out of range");
        }
    }

    int& operator[](int i) {
        if (0 <= i and i < size) {
            return data[i];
        } else {
            throw out_of_range("IndexError");
        }
    }
};

void test_constructor1() {
    cout << "\ntest_constructor1()" << endl;
    ArrayList array;

    cout << "array.size = " << array.size << endl;
    array.append(42);
    cout << "array.size = " << array.size << endl;
    cout << "array.get(array.size-1) = " << array.get(array.size - 1) << endl;
    array.get(array.size - 1) = 2;
    cout << "array.get(array.size-1) = " << array.get(array.size - 1) << endl;
}

void test_constructor2() {
    cout << "\ntest_constructor2()" << endl;
    ArrayList array{1, 2, 3, 4};

    cout << "array.size = " << array.size << endl;
    array.append(42);
    cout << "array.size = " << array.size << endl;
    cout << "array.get(array.size-1) = " << array.get(array.size - 1) << endl;
    array.get(array.size - 1) = 2;
    cout << "array.get(array.size-1) = " << array.get(array.size - 1) << endl;
}

void test_indexing() {
    cout << "\ntest_constructor2()" << endl;
    ArrayList array{1, 2, 3, 4};

    for (int i = 0; i < array.size; i++) {
        cout << "array[" << i << "] = " << array[i] << endl;
    }
}

void append_elements() {
    int capacity = 5;
    ArrayList array(capacity);
    int N = 11;
    cout << "Trying to add " << N << " elementes to array with capacity " << capacity << endl;
    for (int i = 0; i < N; i++) {
        array.append(i);
    }
    cout << "array size " << array.size << endl;

    for (int i = 0; i < array.size; i++) {
        cout << "array[" << i << "] = " << array[i] << endl;
    }
}

int main() {
    test_constructor1();
    test_constructor2();
    test_indexing();
    append_elements();
    return 0;
}