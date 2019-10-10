#include <QCoreApplication>
#include <sstream>
#include <time.h>
#include <string>
#include <fstream>

#include "myarray.h"
#include "testmyarray.h"

using namespace std;

void menu(int argc, char * argv[]);
void randomInsertionSort();
void randomQSort();
void randomShakerSort();
int getArrayLen();
void timeTests();
void timeTestArrays(MyArray (*generator)(int));
void writeVectorsToFile(string filename, vector<double> v1, vector<double> v2, vector<double> v3);
MyArray sameArrayGenerator(int size);
MyArray sortedAscendingGenerator(int size);

const int TESTS_PER_ARRAY_SIZE = 1;
const int MIN_TEST_ARRAY_LEN = 0;
const int MAX_TEST_ARRAY_LEN = 100;
const int ARRAY_LEN_STEP = 50;
const string FILENAME = "../times";

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    MyArray arr = sortedAscendingGenerator(10);
//    arr.randomize();
//    arr.print();
//    MyArray arr2(10);
//    arr2.copy(arr);
//    arr2.print();
    timeTests();
//    menu(argc, argv);

    return 0;
}

void menu(int argc, char * argv[])
{
    TestMyArray testMyArray;
    bool run = true;
    while (run)
    {
        cout << "1 - сортировка случайного масива с помощью алгоритма сортировки вставками" << endl
             << "2 - сортировка случайного масива с помощью алгоритма шейкер-сортировки" << endl
             << "3 - сортировка случайного масива с помощью алгоритма быстрой сортировки" << endl
             << "4 - временной анализ" << endl
             << "5 - тесты" << endl
             << " > ";
        string saction;
        cin >> saction;
        istringstream iss (saction, istringstream::in);
        int action;
        iss >> action;

        switch (action)
        {
            case 1:
                randomInsertionSort();
                break;
            case 2:
                randomShakerSort();
                break;
            case 3:
                randomQSort();
                break;
            case 4:
                timeTests();
                break;
            case 5:
                QTest::qExec(&testMyArray, argc, argv);
                break;
            default:
                run = false;
        }
    }
}

void timeTests()
{
//    timeTestArrays(sameArrayGenerator);
    timeTestArrays(sortedAscendingGenerator);
}

MyArray sameArrayGenerator(int size)
{
    MyArray sameArray(size, 1);
    return sameArray;
}

MyArray sortedAscendingGenerator(int size)
{
    MyArray ascArray(size);
    ascArray.randomize();
    ascArray.quickSort(0, ascArray.getSize() - 1);
    return ascArray;
}

void timeTestArrays(MyArray (*generator)(int))
{
    // Тестируем массивы, заполненные одинаковыми числами
    vector<double> sameTimesInsertion;
    vector<double> sameTimesQsort;
    vector<double> sameTimesShaker;
    for (int i = MIN_TEST_ARRAY_LEN; i <= MAX_TEST_ARRAY_LEN; i += ARRAY_LEN_STEP)
    {
        MyArray array1 = generator(i);
        MyArray array2(i);
        MyArray array3(i);
        array2.copy(array1);
        array3.copy(array1);
        clock_t t1, t2;
        double totalTicks = 0;
        for (int j = 0; j < TESTS_PER_ARRAY_SIZE; ++j)
        {
            t1 = clock();
            array1.insertionSort();
            t2 = clock();
            totalTicks += (t2 - t1) / static_cast<double>(CLOCKS_PER_SEC);
        }
        totalTicks /= TESTS_PER_ARRAY_SIZE;
        sameTimesInsertion.push_back(totalTicks);

        totalTicks = 0;
        for (int j = 0; j < TESTS_PER_ARRAY_SIZE; ++j)
        {
            t1 = clock();
            array2.shakerSort();
            t2 = clock();
            totalTicks += (t2 - t1) / static_cast<double>(CLOCKS_PER_SEC);
        }
        totalTicks /= TESTS_PER_ARRAY_SIZE;
        sameTimesShaker.push_back(totalTicks);

        totalTicks = 0;
        for (int j = 0; j < TESTS_PER_ARRAY_SIZE; ++j)
        {
            t1 = clock();
            array3.quickSort(0, array3.getSize() - 1);
            t2 = clock();
            totalTicks += (t2 - t1) / static_cast<double>(CLOCKS_PER_SEC);
        }
        totalTicks /= TESTS_PER_ARRAY_SIZE;
        sameTimesQsort.push_back(totalTicks);
    }
    writeVectorsToFile(FILENAME, sameTimesInsertion, sameTimesShaker, sameTimesQsort);
}

void writeVectorsToFile(string filename, vector<double> v1, vector<double> v2, vector<double> v3)
{
    ofstream fout(filename);
    if (fout.is_open())
    {
        fout << "Массивы с одинаковыми символами" << endl;
        fout << "Размер массива\t" << "Вставками\t" << "Шейкер\t" << "Быстрая\t" << endl;
        for (int i = 0; i < v1.size(); ++i)
        {
            fout << i * 50 << "\t" << v1.at(i) << "\t\t"
                 << v2.at(i) << "\t\t"
                 << v3.at(i) << endl;
        }
    }
    else
        cout << "Unable to open file " << filename << endl;
}

void randomInsertionSort()
{
    int arrSize = getArrayLen();
    MyArray array(arrSize);
    array.randomize();
    cout << endl;
    cout << "Исходный массив: " << endl;
    array.print();
    array.insertionSort();
    cout << "Отсортированный массив: " << endl;
    array.print();
    cout << endl;
}

void randomQSort()
{
    int arrSize = getArrayLen();
    MyArray array(arrSize);
    array.randomize();
    cout << endl;
    cout << "Исходный массив: " << endl;
    array.print();
    array.quickSort(0, array.getSize() - 1);
    cout << "Отсортированный массив: " << endl;
    array.print();
    cout << endl;
}

void randomShakerSort()
{
    int arrSize = getArrayLen();
    MyArray array(arrSize);
    array.randomize();
    cout << endl;
    cout << "Исходный массив: " << endl;
    array.print();
    array.shakerSort();
    cout << "Отсортированный массив: " << endl;
    array.print();
    cout << endl;
}

int getArrayLen()
{
    string str_size;
    int size = -1;
    while (size < 0)
    {
        cout << "Введите длину массива: " << endl;
        cin >> str_size;
        try {

            size = stoi(str_size);
        } catch (invalid_argument) {
            cout << "Некорректный ввод, попробуйте еще раз." << endl;
        }
    }
    return size;
}
