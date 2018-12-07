#include <iostream>
#include <string>
#include <fstream>
#include "sparsematrix.h"
#include "matrix.h"
#include <limits.h>
#include <time.h>
#include <algorithm>
#include <exception>
#include "myexceptions.h"
#include "functor.h"
#include <cstring>
#include <ctime>

using namespace std;


const int RESULT_OK = 0;
const int RESULT_EXIT = 1;
const int RESULT_OPENFILE_ERROR = 2;
const int RESULT_WRONG_FILE_INPUT = 3;
const int RESULT_WRONG_SIZE = 4;
const int RESULT_ERROR = 5;
const string testilename1 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab_03_DTaS/Database/matrix1";
const string testFilename2 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab_03_DTaS/Database/matrix2";
static string filename1;
static string filename2;

void outInterface();
int menu(SparseMatrix** matrix);
int inputMatrix(SparseMatrix* matrix);
void filesInfo();
string getFilename();
SparseMatrix *getMatrix();
SparseMatrix * readFile();
vector<string> split(string text, char splitter);
bool isUnsignedInt(string str);
size_t inputUnsignedInt(string message);
size_t restrictUnsignedIntInput(string message, size_t r);
void comparePerfomance();
double getDouble();
double getDouble(vector<string>::iterator iter);

int main()
{
    int code = RESULT_OK;
    outInterface();
    static SparseMatrix *sparseMatrix1;
    static SparseMatrix *sparseMatrix2;
    static SparseMatrix sparseResult;

    code = menu(&sparseMatrix1);
    while (code == RESULT_ERROR) {
        code = menu(&sparseMatrix2);
    }
    code = menu(&sparseMatrix2);
    while (code == RESULT_ERROR) {
        code = menu(&sparseMatrix2);
    }

    Matrix *matrix1 = sparseMatrix1->toMatrix();
    Matrix *matrix2 = sparseMatrix2->toMatrix();
    Matrix *resultMatrix;

//    cout << "Исходные разреженные матрицы" << endl;
//    sparseMatrix1->outSparseMatrix();
//    sparseMatrix2->outSparseMatrix();

//    cout << "Исходные матрицы в обычном виде" << endl;
//    matrix1->outMatrix();
//    matrix2->outMatrix();

//    sparseResult = *sparseMatrix1 + sparseMatrix2;
//    cout << "Результат: " << endl;
//    sparseResult.outSparseMatrix();

//    resultMatrix = *matrix1 + matrix2;
//    cout << "Результат: " << endl;
//    resultMatrix->outMatrix();


    long double startTime, endTime, sparseTime, time;
    try
    {
        startTime = clock();
        sparseResult = *sparseMatrix1 + sparseMatrix2;
        endTime = clock();
        cout << "Результат: " << endl;
        sparseResult.outSparseMatrix();
        sparseTime = (endTime - startTime) / CLOCKS_PER_SEC;
    }
    catch (...)
    {
        cout << "Невозможно сложить матрицы разной размерности!" << endl;
        return RESULT_WRONG_SIZE;
    }

    try
    {
        startTime = clock();
        resultMatrix = *matrix1 + matrix2;
        endTime = clock();
        cout << "Результат: " << endl;
        resultMatrix->outMatrix();
        time = (endTime - startTime) / CLOCKS_PER_SEC;
    }
    catch (...)
    {
        cout << "" << endl;
        return RESULT_WRONG_SIZE;
    }

    long double spar1, spar2;
    spar1 = ((sparseMatrix1->columns() * sparseMatrix1->rows()
             - sparseMatrix1->values().size()) * 100.0l) / (sparseMatrix1->columns() * sparseMatrix1->rows());

    spar2 = ((sparseMatrix2->columns() * sparseMatrix2->rows()
             - sparseMatrix2->values().size()) * 100.0l) / (sparseMatrix2->columns() * sparseMatrix2->rows());

    cout << "Размерность матриц: "
         << sparseMatrix1->rows() << "x" << sparseMatrix1->columns()
         << endl;
    cout << "Процент разреженности 1 матрицыы: "
         << spar1
         << endl;
    cout << "Процент разреженности 1 матрицыы: "
         << spar2
         << endl;
    cout << "Время сложения разреженных матриц: " << time <<  endl; //!!
    cout << "Время сложения обычных матриц: " << sparseTime << endl;

    cout << "Затраченная память: " << endl;
    cout << "Для хранения разреженной матрицы: " <<
            sizeof (sparseMatrix1->columns()) +
            sizeof (FirstColumn) * sparseMatrix1->firstInColumn().size() +
            sizeof (size_t) * sparseMatrix1->rowIndex().size() +
            sizeof (sparseMatrix1->rows()) +
            sizeof (double) * sparseMatrix1->values().size()
         << endl;
    cout << "Для хранения обычной матрицы: " <<
            sizeof (double) * matrix1->columns() * matrix1->rows() +
            sizeof (matrix1->columns()) +
            sizeof (matrix1->rows())
         << endl;
    return code;
}

/**
  \throws InvalidDataException
 */
double getDouble(vector<string>::iterator iter)
{
    double result;

    try {
        result = stod(*iter);
    } catch (...) {
        throw InvalidDataException();
    }

    return result;
}

/**
  \throws OpenFileException
  \throws InvalidDataException
 */
SparseMatrix* readFile()
{
    filesInfo();

    string filename = getFilename();
    ifstream fin;
    fin.open(filename);
    if (!fin.is_open())
    {
        cout << "Невозможно открыть файл: ";
        cout << filename << endl;
        throw OpenFileException();
    }

    vector<Item> items;
    size_t rowsCount = 0, columnsCount = 0;
    string buf;
    vector<string> vecStrBuf;
    size_t rows, columns;

    getline(fin, buf);
    vecStrBuf = split(buf, ',');

    if (vecStrBuf.size() == 2 && isUnsignedInt(vecStrBuf[0]) && isUnsignedInt(vecStrBuf[1]))
    {
        rows = stoul(vecStrBuf[0], nullptr, 10);
        columns = stoul(vecStrBuf[1], nullptr, 10);
    }
    else
    {
        throw InvalidDataException ();
    }
    while (!fin.eof() && rowsCount <= rows)
    {
        getline(fin, buf);
        if (buf.empty())
            break;
        vecStrBuf = split(buf, ',');
        if (vecStrBuf.size() != columns)
        {
            fin.close();
            cout << "Некорректные данные в файле!" << endl;
            throw InvalidDataException ();
        }
        columnsCount = 0;
        for (vector<string>::iterator iter = vecStrBuf.begin(); iter != vecStrBuf.end(); iter++)
        {
            double value;
            try {
                value = getDouble(iter);
            } catch (InvalidDataException) {
                cout << "Некорректные данные в файле." << endl;
                throw InvalidDataException();
            }
            if (value != 0.0)
            {
                Item item;
                item.value = value;
                item.row = rowsCount;
                item.column = columnsCount;
                items.push_back(item);
            }
            columnsCount++;
        }
        rowsCount++;
    }
    fin.close();
    return SparseMatrix::initSparseMatrix(&items, rows, columns);
}


bool isUnsignedInt(string str)
{
    for (string::iterator iter = str.begin(); iter != str.end(); iter++)
    {
        if (!isdigit(*iter))
            return false;
    }
    return true;
}

int menu(SparseMatrix **matrix)
{
    cout << "Выберите вариант ввода матрицы: " << endl;
    cout << "\t1 - файл" << endl;
    cout << "\t2 - вручную" << endl;
    cout << ">> ";
    unsigned char answer = 2;
    {
        unsigned short buf;
        cin >> buf;
        answer = static_cast<unsigned char>(buf);
    }
    switch (answer)
    {
    case 1:
        try {
        *matrix = readFile();
        } catch (...) {
            return RESULT_ERROR;
        }
        return RESULT_OK;
    case 2:
        try {
        *matrix = getMatrix();
    } catch (...) {
        return RESULT_ERROR;
    }
        return RESULT_OK;
    default:
        cout << "До встречи!" << endl;
        exit(EXIT_SUCCESS);
    }
}

//Проверка на неравность числу r
size_t restrictUnsignedIntInput(string message, size_t r)
{
    size_t result;
    result = inputUnsignedInt(message);
    while (result == r)
    {
        cout << "Здесь не может быть " << r << "!" << endl;
        result = inputUnsignedInt(message);
    }
    return result;
}

// Ввод матрицы с клавиатуры
SparseMatrix* getMatrix()
{
    vector<Item> items;
    size_t rows = 0, columns = 0, notZeroElements = 0;
    cout << "Формат чисел - целые либо десятичные дроби, разделитель - точка." << endl;
    rows = restrictUnsignedIntInput("Введите количество строк в матрице: ", 0);
    columns = restrictUnsignedIntInput("Введите количество столбцов в матрице: ", 0);
    notZeroElements = restrictUnsignedIntInput("Введите количество ненулевых элементов: ", 0);
    while (notZeroElements > rows * columns)
    {
        cout << "Ненулевых элементов не может быть больше общего количества элементов в матрице!" << endl;
        notZeroElements = restrictUnsignedIntInput("Введите количество ненулевых элементов: ", 0);
    }
    cout << "Далее введите все ненулевые элементы матрицы, индексация начинается с 0." << endl;

    for (size_t i = 0; i < notZeroElements; i++)
    {
        size_t curRow, curCol;
        curRow = inputUnsignedInt("Введите ряд: ");
        while (curRow > rows - 1)
        {
            cout << "Индекс выходит за границы матрицы!" << endl;
            curRow = inputUnsignedInt("Введите ряд: ");
        }
        curCol = inputUnsignedInt("Введите колонку: ");
        while (curCol > columns - 1)
        {
            cout << "Индекс выходит за границы матрицы!" << endl;
            curCol = inputUnsignedInt("Введите колонку: ");
        }
        double value = getDouble();
        Item curItem;
        curItem.column = curCol;
        curItem.row = curRow;
        curItem.value = value;
        items.push_back(curItem);
    }
  return SparseMatrix::initSparseMatrix(&items, rows, columns);
}

double getDouble()
{
    double result;
    bool flag = false;

    string buff;

    while (!flag) {
        cout << "Введите элемент: ";
        cin >> buff;
        try {
            result = stod(buff);
            flag = true;
        } catch (...) {
            cout << "Некорректный ввод!" << endl;
        }
    }
    return result;
}

size_t inputUnsignedInt(string message)
{
    string buf;
    size_t result = 0;
    cout << message;
    cin >> buf;
    while (!(isUnsignedInt(buf) && buf.size() <= to_string(UINT_MAX).size() - 1))
    {
        if (buf.size() > to_string(UINT_MAX).size() - 1)
        {
            cout << "Слишком большое число!" << endl;
        }
        else if (!isUnsignedInt(buf))
        {
            cout << "Некорректный ввод!" << endl;
        }
        cout << message;
        cin >> buf;
    }
    result = stoul(buf, nullptr, 10);
    return result;
}

void filesInfo()
{
    cout << "В первой строке файла должно быть указано только число строк и столбцов!" << endl;
    cout << "Все числа в файле должны быть написаны через запятую!" << endl;
    cout << "Формат чисел - целые либо десятичные дроби, разделитель - точка." << endl;
}

string getFilename()
{
    string filename;
    cout << "Введите имя файла: ";
    cin >> filename;
    if (filename1.empty())
        filename1 = filename;
    else
    {
        while (strcmp(filename1.c_str(), filename.c_str()) == 0)
        {
            cout << "Неверное имя файла!" << endl;
            cout << "Введите имя файла: ";
            cin >> filename;
        }
        filename2 = filename;
    }
    return filename;
}

void outInterface()
{
    cout << "Программа реализует операцию сложения двух матриц." << endl;
}

vector<string> split(string text, char splitter)
{
  string buffer;
  vector<string> strings;
  for (const char c : text)
  {
      if (c != splitter) buffer.push_back(c);
      else
      {
          strings.push_back(buffer);
          buffer.clear();
      }
    }
  if(!buffer.empty()) strings.push_back(buffer);
  return strings;
}
