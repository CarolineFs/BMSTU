#ifndef MYARRAY_H
#define MYARRAY_H

#include <iostream>
#include <stdexcept>
#include <stdlib.h>
#include <ctime>
#include <vector>

class MyArray
{
public:
    MyArray(int s, int defaultValue=0);
    MyArray(int s, std::initializer_list<int> l);
    MyArray(int s, int *arr);
    MyArray(std::vector<int> &vec);
//    MyArray& operator=(const MyArray &arr);
    ~MyArray();
    int getSize() const;
    int at(int index);
    void randomize(int minVal=-50, int range=100);
    void insert(int value, int index);
    void insertionSort();
    void quickSort(int first, int last);
    void shakerSort();
    bool compare(MyArray &toCompare);
    bool compare(MyArray &toCompare1, MyArray &toCompare2);
    void print();
    void copy(const MyArray& arr);
private:
    int pivotList(int* list, int first, int last);
    int size;
    int* array;
};

#endif // MYARRAY_H
