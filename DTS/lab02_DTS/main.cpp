#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <limits.h>
#include <ctime>

#define SerializedName(x) find(x, buff)
#define init(x) buff = x

using namespace std;

#ifdef _WIN32 || _WIN64
const string FILENAME = "";
#else
const string FILENAME = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS";
const string FILENAME20 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS_20";
const string FILENAME80 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS_80";
const string FILENAME160 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS_160";
const string FILENAME320 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS_320";
const string FILENAME1000 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS_1000";
const string FILENAME2000 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS_2000";
const string FILENAME4000 = "/home/syzygy/Desktop/Labs/Data_Types_and_Structures/lab02_DTS/Database/lab02_DTS_4000";

const string FILES[] = { FILENAME20,
                         FILENAME,
                         FILENAME80,
                         FILENAME160,
                         FILENAME320,
                         FILENAME1000,
                         FILENAME2000,
                         FILENAME4000 };
#endif
const string ID = "Id";
const string BRAND = "Brand";
const string MANUFACTURER = "Manufacturer";
const string PRICE = "Price";
const string COLOR = "Color";
const string CONDITION = "Condition";
const string GUARANTEE = "Guarantee";
const string ISSUE_YEAR = "IssueYear";
const string MILEAGE = "Mileage";
const string REPAIRS = "Repairs";
const string OWNERS = "Owners";
static string buff;

struct NewCar
{
    long int guarantee;
};
struct OldCar
{
    long int issueYear;
    long int mileage;
    long int repairs;
    long int owners;
};
union Condition
{
    NewCar newCar;
    OldCar oldCar;
};
struct Car
{
    long int id;
    string brand;
    string manufacturer;
    long int price;
    string color;
    string cond;
    Condition condition;
};

static vector<Car> CARS;

Car parce(string);
//vector<string> split(string, char);
string find(string, string);
void printInformation();
int addRecord();
int deleteRecord();
int filterOldCars();
vector<pair<size_t, string>> sortKeys(vector<pair<size_t, string>>);
int sortInitialTable();
vector<Car> sortCarsBinarySearch(vector<Car>);
int sortKeysShowInitial();
vector<pair<size_t, string>> sortKeysBinarySearch(vector<pair<size_t, string>>);
int comparePerformance();
bool checkInt(string);
vector<Car> readDatabase(string);
long int inputInt(string);
long int inputItem(string);
void writeDatabase(Car);
int getLastId();
int showSortedKeys();
vector<pair<size_t, string>> getKeys(vector<Car>);
string operatorAsterisk(string, size_t);
vector<Car> sortCars(vector<Car>);
void outCar(Car);
void outTableHead();
void showTable();
int menu();
int inputString(string*, string);
void tickTime(long*, long*, vector<Car>);
void tickTimeTable(long*, long*, vector<Car>);

int main()
{
    printInformation();
    CARS = readDatabase(FILENAME);
    while (!menu());
    return 0;
}

int menu()
{
    unsigned char aswer;
    {
        unsigned short buf;
        cout << ">> ";
        cin >> buf;
        aswer = static_cast<unsigned char>(buf);
    }
    switch (aswer)
    {
    case 1:
        filterOldCars();
        return 0;
    case 2:
        addRecord();
        return 0;
    case 3:
        deleteRecord();
        return 0;
    case 4:
        showSortedKeys();
        return 0;
    case 5:
        sortInitialTable();
        return 0;
    case 6:
        sortKeysShowInitial();
        return 0;
    case 7:
        comparePerformance();
        return 0;
    case 9:
        showTable();
        return 0;
    default:
        cout << "До встречи!" << endl;
        return 1;
    }
}

int inputString(string* ptrString, string message)
{
    cout << "Длина строки не более 50 букв." << endl;
    while (1)
    {
        cout << message;
        cin >> *ptrString;
        if ((*ptrString).size() <= 50) break;
        cout << "Слишком длинная строка." << endl;
    }
    return 0;
}

void showTable()
{
    CARS = readDatabase(FILENAME);
    outTableHead();
    for (vector<Car>::iterator iter = CARS.begin(); iter != CARS.end(); iter++)
        outCar(*iter);
}

int sortInitialTable()
{
    CARS = sortCarsBinarySearch(CARS);
    cout << operatorAsterisk("-", 125) << endl;
    outTableHead();
    for (vector<Car>::iterator iter = CARS.begin(); iter != CARS.end(); iter++)
        outCar(*iter);
    return 0;
}

vector<Car> sortCarsBinarySearch(vector<Car> cars)
{
    // Сортировка бинарными вставками

    int n = cars.size();
    for (int i = 1; i < n; i++)
    {
        if (cars[i-1].brand > cars[i].brand)
        {
            struct Car x = cars[i];
            int left = 0;
            int right = i - 1;
            while (1)
            {
                int sred = (left + right) / 2;
                if (cars[sred].brand < x.brand)
                    left = sred + 1;
                else
                    //if (sred != 0)
                        right = sred - 1;
                if (left > right)
                    break;
            }
            int j = i - 1;
            while (j >= left)
            {
                swap(cars[j+1], cars[j]);
                j--;
            }
            cars[left] = x;
        }
    }
    return cars;
}

vector<Car> sortCars(vector<Car> cars)
{
    // Шейкер сортировка
    int n = cars.size();
    for (int i = 1; i < n; i++)
    {
        if (cars[i-1].brand > cars[i].brand)
        {
            struct Car x = cars[i];
            int left = 0;
            int right = i - 1;
            while (1)
            {
                int sred = (left + right) / 2;
                if (cars[sred].brand < x.brand)
                    left = sred + 1;
                else
                    right = sred - 1;
                if (left > right)
                    break;
            }
            int j = i - 1;
            while (j >= left)
            {
                swap(cars[j+1], cars[j]);
                j--;
            }
            cars[left] = x;
        }
    }
    return cars;
}

int sortKeysShowInitial()
{
    vector<pair<size_t, string>> sortedKeys = sortKeys(getKeys(CARS));
    cout << operatorAsterisk("-", 125) << endl;
    outTableHead();
    for (vector<pair<size_t, string>>::iterator iter = sortedKeys.begin(); iter != sortedKeys.end(); iter++)
        outCar(CARS[(*iter).first]);
    return 0;
}

void outCar(Car currentCar)
{
    cout << "|"
         << currentCar.id << operatorAsterisk(" ", 6 - to_string(currentCar.id).size()) << "|"
         << currentCar.brand << operatorAsterisk(" ", 20 -currentCar.brand.size()) << "|"
         << currentCar.manufacturer << operatorAsterisk(" ", 15 -currentCar.manufacturer.size()) << "|"
         << currentCar.price << operatorAsterisk(" ", 15 - to_string(currentCar.price).size()) << "|"
         << currentCar.color << operatorAsterisk(" ", 15 - currentCar.color.size()) << "|";
    if (currentCar.cond == "new")
        cout << currentCar.condition.newCar.guarantee
             << operatorAsterisk(" ", 37 - to_string(currentCar.condition.oldCar.issueYear).size()) << "|"
             << endl;
    else
        cout << currentCar.condition.oldCar.issueYear
             << operatorAsterisk(" ", 6 - to_string(currentCar.condition.oldCar.issueYear).size()) << "|"
             << currentCar.condition.oldCar.mileage
             << operatorAsterisk(" ", 10 - to_string(currentCar.condition.oldCar.mileage).size()) << "|"
             << currentCar.condition.oldCar.repairs
             << operatorAsterisk(" ", 6 - to_string(currentCar.condition.oldCar.repairs).size()) << "|"
             << currentCar.condition.oldCar.owners
             << operatorAsterisk(" ", 6 - to_string(currentCar.condition.oldCar.owners).size()) << "|"
             << endl;
    cout << operatorAsterisk("-", 125) << endl;
}

int comparePerformance()
{
    cout << "Сравнение эффективности алгоритмов сортировки: " << endl
         << "    шейкер-сортировка и сортировка бинарными вставками." << endl;

    cout << "Сортировка ключей (время в секундах)." << endl;
    cout << operatorAsterisk("-", 114) << endl;
    cout << "|    " << "Размер таблицы    |" << "        Шейкер        |"
         << "   Бинарные вставки   |"
         << " Памяти занято        |"
         << " Среднее время        |"
         << endl;
    cout << operatorAsterisk("-", 114) << endl;
    long t1, t2, averSkake1 = 0, averShake2 = 0, averBin1 = 0, averBin2 = 0;
    vector<Car> currentCars;
    for (size_t i = 0; i < 8; i++)
    {
        currentCars = readDatabase(FILES[i]);
        tickTime(&t1, &t2, currentCars);
        averSkake1 += t1;
        averBin1 += t2;
        unsigned long size = sizeof (getKeys(currentCars)[0]) * getKeys(currentCars).size();
        double m = (t1 + t2) / 2.0 ;
        cout << "| " << currentCars.size() << operatorAsterisk(" ", 19 - to_string(currentCars.size()).size()) << "|"
             << " " << t1 << operatorAsterisk(" ", 19 - to_string(t1).size()) << "|"
             << " " << t2 << operatorAsterisk(" ", 19 - to_string(t2).size()) << "|"
             << " " << size
             << operatorAsterisk(" ", 19 - to_string(size).size()) << "|"
             << " " << m << operatorAsterisk(" ", 26 - to_string(m).size())
             << endl;
        cout << operatorAsterisk("-", 114) << endl;
    }

    cout << "Сортировка таблицы." << endl;
    cout << operatorAsterisk("-", 114) << endl;
    cout << "|    " << "Размер таблицы    |" << "        Шейкер        |"
         << "   Бинарные вставки   |"
         << " Памяти занято        |"
         << " Среднее время        |"
         << endl;
    cout << operatorAsterisk("-", 114) << endl;
    for (size_t i = 0; i < 8; i++)
    {
        currentCars = readDatabase(FILES[i]);
        tickTimeTable(&t1, &t2, currentCars);
        averShake2 += t1;
        averBin2 += t2;
        unsigned long size = sizeof (currentCars[0]) * currentCars.size();
        double m = (t1 + t2) / 2 ;
        cout << "| " << currentCars.size() << operatorAsterisk(" ", 19 - to_string(currentCars.size()).size()) << "|"
             << " " << t1 << operatorAsterisk(" ", 19 - to_string(t1).size()) << "|"
             << " " << t2 << operatorAsterisk(" ", 19 - to_string(t2).size()) << "|"
             << " " << size << operatorAsterisk(" ", 19 - to_string(size).size()) << "|"
             << " " << m << operatorAsterisk(" ", 26 - to_string(m).size())
             << endl;
        cout << operatorAsterisk("-", 114) << endl;
    }

    cout << "ЗАКЛЮЧЕНИЕ" << endl;
    double percent = (100.0 * sizeof (getKeys(readDatabase(FILENAME))[0]) * getKeys(readDatabase(FILENAME)).size()) /
            (sizeof (readDatabase(FILENAME)[0]) * readDatabase(FILENAME).size());
    cout << "Сортировка таблицы ключей занимает на " << percent << "% больше памяти." << endl;
    percent = (100.0 * averBin1) / averSkake1;
    cout << "Сортировка главной таблицы бинарными вставками быстрее шейкер-сортировка на " << percent << "%." << endl;
    percent = (100.0 * averBin2) / averShake2;
    cout << "Сортировка главной таблицы бинарными вставками быстрее шейкер-сортировка на " << percent << "%." << endl;
    percent = (100.0 * ((averBin1 + averSkake1)/2.0)) / ((averBin2 + averShake2)/2.0);
    cout << "Сортировка таблицы ключей быстрее сортировки главной таблицы в среднем на " << percent << "%." << endl;
    return 0;
}

void tickTime(long* t1, long* t2, vector<Car> cars)
{
    long start_time, end_time;
    start_time = clock();
    sortKeys(getKeys(cars));
    end_time = clock();
    *t1 = end_time - start_time;
    start_time = clock();
    sortKeysBinarySearch(getKeys(cars));
    end_time = clock();
    *t2 = end_time - start_time;
}

void tickTimeTable(long* t1, long* t2, vector<Car> cars)
{
    vector<Car> copy = cars;
    long start_time, end_time;
    start_time = clock();
    cars = sortCars(cars);
    end_time = clock();
    *t1 = end_time - start_time;
    start_time = clock();
    cars = sortCarsBinarySearch(copy);
    end_time = clock();
    *t2 = end_time - start_time;
}

int addRecord()
{
    string brand, manufacturer, color, condition;
    long int price;

    inputString(&brand, "Введите марку: ");
    inputString(&manufacturer, "Введите страну-производителя: ");
    inputString(&color, "Введите цвет: ");
    price = inputItem("Введите цену: ");
    condition = "";
    while (1) {
        cout << "Введите состояние (новая/старая): ";
        cin >> condition;
        if ((condition == "новая") || (condition == "старая")) break;
        else cout << "Некорректный ввод. Попробуйте снова." << endl;
    }
    Car newCar;
    newCar.brand = brand;
    newCar.color = color;
    newCar.manufacturer = manufacturer;
    newCar.id = getLastId() + 1;
    condition == "новая" ? newCar.cond = "new" : newCar.cond = "old";
    newCar.price = price;
    if (condition == "новая")
    {
        long int guarantee;
        guarantee = inputItem("Введите гарантию: ");
        newCar.condition.newCar.guarantee = guarantee;
    }
    else
    {
        long int issueYear, mileage, repairs, owners;
        issueYear = inputItem("Введите год выпуска: ");
        mileage = inputItem("Введите пробег: ");
        repairs = inputItem("Введите количество ремонтов: ");
        owners = inputItem("Введите количество владельцев: ");
        newCar.condition.oldCar.issueYear = issueYear;
        newCar.condition.oldCar.mileage = mileage;
        newCar.condition.oldCar.owners = owners;
        newCar.condition.oldCar.repairs = repairs;
    }
    CARS.push_back(newCar);
    writeDatabase(newCar);
    return 0;
}

void writeDatabase(Car car)
{
    string str;
    str = "{ " + ID + ": \"" + to_string(car.id) + "\", " +
            BRAND + ": \"" + car.brand + "\", " +
            MANUFACTURER + ": \"" + car.manufacturer + "\", " +
            PRICE + ": \"" + to_string(car.price) + "\", " +
            COLOR + ": \"" + car.color + "\", " +
            CONDITION + ": \"" + car.cond + "\", ";
    if (car.cond == "new") str += GUARANTEE + ": \"" + to_string(car.condition.newCar.guarantee) +
            "\" },";
    else str += ISSUE_YEAR + ": \"" + to_string(car.condition.oldCar.issueYear) + "\", " +
            MILEAGE + ": \"" + to_string(car.condition.oldCar.mileage) + "\", " +
            REPAIRS + ": \"" + to_string(car.condition.oldCar.repairs) + "\", " +
            OWNERS + ": \"" + to_string(car.condition.oldCar.owners) + "\" },";
    ofstream out;
    out.open(FILENAME, ios::app);
    if (out.is_open())
    {
        out << str << endl;
        //cout << "Новая машина внесена в базу даных." << endl;
    }
    else
    {
        cout << "Невозможно открыть файл:\n" << FILENAME << endl;
    }
    out.close();
}

long int inputItem(string message)
{
    long int res;
    res = inputInt(message);
    while (res == -1)
    {
        cout << "Некорректный ввод. Попробуйте еще раз." << endl;
        res = inputInt(message);
    }
    return  res;
}

int deleteRecord()
{
    cout << "Удаление записи по ID." << endl;
    long int id;
    id = inputItem("Введите id автомобиля, который необходимо удалить: ");
    bool flag = false;
    for (vector<Car>::iterator iter = CARS.begin(); iter != CARS.end(); iter++)
        if ((*iter).id == id)
        {
            CARS.erase(iter);
            flag = true;
            break;
        }
    if (!flag)
    {
        cout << "Не удалось найти автомобиль с таким id." << endl;
        return -1;
    }
    ofstream out;
    out.open(FILENAME, ios_base::trunc);
    out.close();
    for (vector<Car>::iterator iter = CARS.begin(); iter != CARS.end(); iter++)
        writeDatabase(*iter);
    cout << "Запись удалена из базы данных." << endl;
    return 0;
}


int showSortedKeys()
{
    vector<pair<size_t, string>> sortedKeys = sortKeys(getKeys(CARS));
    cout << "Отсортированная таблица ключей" << endl;
    cout << operatorAsterisk("-", 32) << endl;
    cout << "| Индекс |" << "  Марка                |" << endl;
    cout << operatorAsterisk("-", 32) << endl;
    for (vector<pair<size_t, string>>::iterator iter = sortedKeys.begin(); iter != sortedKeys.end(); iter++)
        cout << "|"
             << " " << (*iter).first << operatorAsterisk(" ", 5 - to_string((*iter).first).size())
             << "|"
             << " " << (*iter).second << operatorAsterisk(" ", 20 - (*iter).second.size())
             << "|"
             << endl;
    cout << operatorAsterisk("-", 32) << endl;
    return 0;
}

string operatorAsterisk(string str, size_t n)
{
    string copy = str;
    for (size_t i = 0; i <= n; i++)
        str += copy;
    return str;
}

vector<pair<size_t, string>> getKeys(vector<Car> cars)
{
    vector<pair<size_t, string>> keys;

    for (size_t i = 0; i < cars.size(); i++)
    {
        keys.push_back(make_pair(i, cars[i].brand));
    }
    return keys;
}

vector<pair<size_t, string>> sortKeysBinarySearch(vector<pair<size_t, string>> keys)
{
    // Сортировка бинарными вставками

    int n = keys.size();
    for (int i = 1; i < n; i++)
    {
        if (keys[i-1].second > keys[i].second)
        {
            pair<size_t, string> x = keys[i];
            int left = 0;
            int right = i - 1;
            while (1)
            {
                int sred = (left + right) / 2;
                if (keys[sred].second < x.second)
                    left = sred + 1;
                else
                    right = sred - 1;
                if (left > right)
                    break;
            }
            int j = i - 1;
            while (j >= left)
            {
                swap(keys[j+1], keys[j]);
                j--;
            }
            keys[left] = x;
        }
    }
    return keys;
}

vector<pair<size_t, string>> sortKeys(vector<pair<size_t, string>> keys)
{
    // Шейкер сортировка

    for (size_t left_idx = 0, right_idx = keys.size() - 1; left_idx < right_idx;)
    {
        for (size_t idx = left_idx; idx < right_idx; idx++)
        {
            if (keys[idx + 1].second < keys[idx].second)
            {
                swap(keys[idx], keys[idx + 1]);
            }
        }
        right_idx--;
        for (size_t idx = right_idx; idx > left_idx; idx--)
        {
            if (keys[idx - 1].second > keys[idx].second)
            {
                swap(keys[idx - 1], keys[idx]);
            }
        }
        left_idx++;
    }
    return keys;
}

int filterOldCars()
{
    string brand;
    string s;
    long int min, max;
    inputString(&brand, "Введите марку автомобиля: ");
    cout << "Цена - целое число." << endl;
    min = inputItem("Введите минимальную цену в рублях: ");
    max = inputItem("Введите максимальную цену в рублях: ");
    if (min == -1 || max == -1) return -1;
    if (min > max) { cout << "Минимум больше максимума.\nЗавершение..." << endl; return -1; }
    bool flag = false;
    for (vector<Car>::iterator iter = CARS.begin(); iter != CARS.end(); iter++)
    {
        if ((*iter).brand == brand && (*iter).cond == "old" && (*iter).condition.oldCar.repairs == 0
                && (*iter).condition.oldCar.owners == 1 && (*iter).price <= max && (*iter).price >= min)
        {
            if (!flag) outTableHead();
            flag = true;
            cout << operatorAsterisk("-", 125) << endl;
            outCar(*iter);
        }
    }
    if (!flag) cout << "Ни один автомобиль не соответствет условиям поиска." << endl;

    return 0;
}

long int inputInt(string message)
{
    string s;
    long int res;
    cout << message;
    cin >> s;
    if (!checkInt(s)) { return -1; }//{ cout << "Некорректный ввод.\nЗавершение..." << endl; return -1; }
    if (s.size() > to_string(LONG_MAX).size()) { cout << "Слишком большое число." << endl; return -1; }
    res = strtol(s.c_str(), NULL, 10);
    return res;
}

vector<Car> readDatabase(string filename)
{
    vector<Car> cars;
    ifstream fin;
    string buf;
    fin.open(filename);
    if (!fin.is_open()) { cout << "Невозможно открыть файл:\n " << filename << endl; return cars; }
    while (!fin.eof()) {
        getline(fin, buf);
        if (buf.size() == 0) break;
        cars.push_back(parce(buf));
    }
    fin.close();
    return cars;
}

string find(string str, string totalString)
{
  size_t start =totalString.find(str);
  while (totalString[start++] != '"');

  size_t last = start+1;
  while (totalString[last] != '"') ++last;

  return totalString.substr(start, last - start);
}

Car parce(string str)
{
    Car result;
    init(str);
    string id = SerializedName(ID);
    result.id = stoi(id, NULL, 10);
    result.brand = SerializedName(BRAND);
    result.manufacturer = SerializedName(MANUFACTURER);
    result.price = stol(SerializedName(PRICE));
    result.color = SerializedName(COLOR);
    result.cond = SerializedName(CONDITION);
    if (result.cond == "new")
    {
        result.condition.newCar.guarantee = stoi(SerializedName(GUARANTEE));
    }
    else
    {
        result.condition.oldCar.issueYear = stoi(SerializedName(ISSUE_YEAR));
        result.condition.oldCar.mileage = stoi(SerializedName(MILEAGE));
        result.condition.oldCar.owners = stoi(SerializedName(OWNERS));
        result.condition.oldCar.repairs = stoi(SerializedName(REPAIRS));
    }
    return result;
}

void printInformation()
{
    cout << "Список машин, имеющихся в автомагазине." << endl;
    cout << "1 - Вывести цены не новых"
         << "машин указанной марки с одним предыдущим собственником,"
         << "отсутствием ремонта в указанном диапазоне цен" << endl;
    cout << "2 - добавить новую запись" << endl;
    cout << "3 - удалить запись" << endl;
    cout << "4 - просмотр отсортированной таблицы ключей при несортированной исходной таблице" << endl;
    cout << "5 - вывод упорядоченной исходной таблицы" << endl;
    cout << "6 - вывод исходной таблицы в упорядоченном виде, используя упорядоченную таблицу ключей" << endl;
    cout << "7 - вывод результатов сравнения эффективности работы программы при"
         << "обработке данных в исходной таблице и в таблице ключей" << endl;
    cout << "9 - показать исходную таблицу" << endl;
}

bool checkInt(string str)
{
    for (string::iterator iter = str.begin(); iter != str.end(); iter++)
    {
        if (!isdigit(*iter)) return false;
    }
    return true;
}

int getLastId()
{
    int lastId = -1;
    int currentId = -1;
    ifstream fin;
    string buf;
    fin.open(FILENAME);
    if (!fin.is_open()) { cout << "Невозможно открыть файл:\n " << FILENAME << endl; return -1; }
    while (!fin.eof()) {
        getline(fin, buf);
        if (buf.size() == 0) break;
        buf = SerializedName(ID);
        if (currentId == -1)
        {
            currentId = stoi(buf, NULL, 10);
            lastId = currentId;
        }
        else if (currentId > lastId)
            lastId = currentId;
    }
    fin.close();
    return lastId;
}

void outTableHead()
{
    cout << operatorAsterisk("-", 125) << endl;
    cout << "|  " << ID << "    " << "|"
         << " " << BRAND << operatorAsterisk(" ", 20 - BRAND.size() - 1) << "|"
         << " " << MANUFACTURER << operatorAsterisk(" ", 15 - MANUFACTURER.size() - 1 ) << "|"
         << " " << PRICE << operatorAsterisk(" ", 15  - PRICE.size() - 1) << "|"
         << " " << COLOR << operatorAsterisk(" ", 15 - COLOR.size() - 1) << "|"
         << "  G/Y   " << "|"
         << " " << MILEAGE << operatorAsterisk(" ", 10 - MILEAGE.size() - 1) << "|"
         << " OWN    " << "|"
         << "  REP   " << "|"
         << endl;
    cout << operatorAsterisk("-", 125) << endl;
}
