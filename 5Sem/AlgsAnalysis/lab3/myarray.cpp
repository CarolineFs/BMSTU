#include "myarray.h"

MyArray::MyArray(int s, int defaultValue)
{
    if (s < 0)
        throw std::bad_alloc();
    this->array = (int*) malloc(sizeof(int) * s);
    this->size = s;
    for (int i = 0; i < s; ++i)
        array[i] = defaultValue;
    srand(time(nullptr));
}

MyArray::MyArray(int s, std::initializer_list<int> l)
{
    if (s < 0)
        throw std::bad_alloc();
    if (s > l.size())
        throw std::out_of_range("Список инициализации короче заявленной длины массива.");
    this->array = (int*) malloc(sizeof(int) * s);
    this->size = s;
    int i = 0;
    for(auto& item : l)
    {
        array[i++] = item;
    }
    srand(time(nullptr));
}

MyArray::MyArray(int s, int *arr)
{
    if (s < 0)
        throw std::bad_alloc();
    this->array = (int*) malloc(sizeof(int) * s);
    this->size = s;

    for (int i = 0; i < s; ++i)
        this->array[i] = arr[i];
    srand(time(nullptr));
}

MyArray::MyArray(std::vector<int> &vec)
{
    this->size = vec.size();
    this->array = (int*) malloc(sizeof(int) * this->size);
    for (int i = 0; i < this->size; ++i)
        this->array[i] = vec.at(i);
    srand(time(nullptr));
}

MyArray::~MyArray()
{
    free(array);
}

int MyArray::getSize() const
{
    return size;
}

int MyArray::at(int index)
{
    if (index >= size)
        throw std::out_of_range("Array index out of range.\n");
    return array[index];
}

void MyArray::randomize(int minVal, int range)
{
    for (int i = 0; i < this->size; ++i)
    {
        int randVal = minVal + rand() % range;
        this->array[i] = randVal;
    }
}

void MyArray::insert(int value, int index)
{
    if (index >= size)
        throw std::out_of_range("Array index out of range.\n");
    array[index] = value;
}

void MyArray::insertionSort()
{
    int newElement, location;
    for (int i = 1; i < size; ++i)
    {
        newElement = array[i];
        location = i;

        while (location > 0 && array[location - 1] > newElement)
        {
            array[location] = array[location - 1];
            location -= 1;
        }
        array[location] = newElement;
    }
}

void MyArray::quickSort(int first, int last)
{
    int pivot;
    if (first < last)
    {
        pivot = pivotList(array, first, last);
        quickSort(first, pivot);
        quickSort(pivot + 1, last);
    }
}

void MyArray::shakerSort()
{
    for (int left = 0, right = this->size - 1; left < right;)
    {
        for (int i = left; i < right; ++i)
            if (array[i + 1] < array[i])
                std::swap(array[i], array[i + 1]);
        right--;
        for (int i = right; i > left; --i)
            if (array[i - 1] > array[i])
                std::swap(array[i - 1], array[i]);
        left++;
    }
}

bool MyArray::compare(MyArray &toCompare)
{
    if(this->size != toCompare.size)
        return false;
    for (int i = 0; i < this->size; ++i)
    {
        if (this->array[i] != toCompare.array[i])
            return false;
    }
    return true;
}

int MyArray::pivotList(int* list, int first, int last)
{
    int pivotValue = list[first];
    int pivotPoint = first;
    for (int i = first + 1; i <= last; ++i)
    {
        if (list[i] < pivotValue)
        {
            pivotPoint++;
            std::swap(list[pivotPoint], list[i]);
        }
    }
    std::swap(list[first], list[pivotPoint]);
    return pivotPoint;
}

void MyArray::print()
{
    for (int i = 0; i < size; ++i)
    {
        std::cout << this->array[i] << "  ";
    }
    std::cout << std::endl;
}

void MyArray::copy(const MyArray& arr)
{
    if (arr.size != this->size)
        throw std::out_of_range("Different arrays size to copy.");
    for (int i = 0; i < this->size; ++i)
        this->array[i] = arr.array[i];
}

bool MyArray::compare(MyArray &toCompare1, MyArray &toCompare2)
{
    if (this->size != toCompare1.size ||
            this->size != toCompare2.size ||
            toCompare1.size != size)
        return false;

    for (int i = 0; i < this->size; ++i)
    {
        if (this->array[i] != toCompare1.array[i] ||
            this->array[i] != toCompare2.array[i] ||
            toCompare1.array[i] != toCompare2.array[i])
        {
            return false;
        }
    }
    return true;
}
