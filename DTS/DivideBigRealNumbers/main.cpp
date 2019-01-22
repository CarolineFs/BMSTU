#include <iostream>
#include <string>
#include <locale.h>
#include "mystring.h"
#include <stdlib.h>
#include <vector>
#include <limits>

using namespace std;
using std::vector;
typedef MyString String;

const unsigned int TOO_BIG_MANTISSA = 1;
const unsigned int WRONG_SYMBOL = 3;
const unsigned int TOO_BIG_ORDER = 1;
const unsigned int TOO_SMALL_ORDER = 2;

struct BigReal{
  vector<short> mantissa;
  long long int order;
  short mantissaSign;
};

vector<short> round(vector<short>);
bool isEqual(vector<short>, vector<short>);
vector<short> deleteZeros(vector<short>);
string stringByNumber(string, size_t);
int checkMantissa(string);
int checkOrder(string);
void printHead();
void inputMember(string*, string*, string);
vector<short> convertMantissaToVector(string);
BigReal divide(BigReal, BigReal);
bool isZero(vector<short>);
void handleMantissas(string*, string*);
bool hasPoint(string);
string deleteInsignificantZeros(const string);
vector<short> divideMantissas(vector<short>, vector<short>, long long int*, bool*);
bool isFirstGreater(vector<short>, vector<short>);
vector<short> add(vector<short>, short);
vector<short> subtractNumericalStrings(vector<short>, vector<short>);
bool isBiggest(vector<short>);
void showResult(BigReal);
vector<short> deleteStartZeros(vector<short>);

int main()
{
  string strDividendMantissa;
  string strDividendOrder;
  string strDividerMantissa;
  string strDividerOrder;
  long long int intDividendOrder;
  long long int intDividerOrder;
  short dividentMantissaSign;
  short dividerMantisaSign;
  vector<short> dividendMantissa;
  vector<short> dividerMantissa;
  //setlocale(LC_ALL, "Russian");
  printHead(); //Печатаем информацию о программе
  // Ввод делимого и делителя
  inputMember(&strDividendMantissa, &strDividendOrder, "Input a divident: ");
  inputMember(&strDividerMantissa, &strDividerOrder, "\nInput a divider:\n");
  // Определяем знаки мантиссы делителя и делимого
  dividentMantissaSign = (strDividendMantissa[0] == '-' )? -1 : 1;
  dividerMantisaSign = (strDividerMantissa[0] == '-') ? -1 : 1;
  // Отделяем минусы от мантисс, если они есть
  strDividendMantissa[0] == '-' ? strDividendMantissa.replace(0, 1, "") : strDividendMantissa;
  strDividerMantissa[0] == '-' ? strDividerMantissa.replace(0, 1, "") : strDividerMantissa;
  handleMantissas(&strDividendMantissa, &strDividerMantissa);
  strDividendMantissa = deleteInsignificantZeros(strDividendMantissa);
  strDividerMantissa = deleteInsignificantZeros(strDividerMantissa);
  // Преобразуем мантиссы в векторы
  dividendMantissa = convertMantissaToVector(strDividendMantissa);
  dividerMantissa = convertMantissaToVector(strDividerMantissa);
  // Преобразуем порядки в long long int
  intDividendOrder = atoll(strDividendOrder.c_str());
  intDividerOrder = atoll(strDividerOrder.c_str());
  if (strDividerMantissa == "0")
  {
    cout << "Dividing by zero.\nQuitting..." << endl;
    exit(-1);
  }
  BigReal dividend;
  BigReal divider;
  BigReal result;
  dividend.mantissa = dividendMantissa;
  dividend.order = intDividendOrder;
  dividend.mantissaSign = dividentMantissaSign;
  divider.mantissa = dividerMantissa;
  divider.order = intDividerOrder;
  divider.mantissaSign = dividerMantisaSign;
  result = divide(dividend, divider);
  showResult(result);
  return 0;
}

void showResult(BigReal result)
{
  /* Выводит в консоль результат */
  cout << "Result: " << ((result.mantissaSign == 1) ? "" : "-") << "0.";
  for (size_t i = 0; i < result.mantissa.size(); i++)
    cout << result.mantissa[i];
  cout << " E " << result.order << endl;
}

BigReal divide(BigReal dividend, BigReal divider)
{
  /* Функция деления BIgReal на BIgReal */
  try {
    if (isZero(divider.mantissa)) throw (0);
  } catch (int) {
    cout << "Dividing by zero.\nQuitting..." << endl;
    exit(-1);
  }
  long long int resultOrder = dividend.order - divider.order + 1;
  BigReal result;
  long long int unterimOrder = 0;
  bool hasPoint = false;
  short resultMantissaSign = dividend.mantissaSign * divider.mantissaSign;
  vector<short> resultMantissa;
  vector<short> mantissaAfterPoint;
  resultMantissa = divideMantissas(dividend.mantissa, divider.mantissa, &unterimOrder, &hasPoint);
  //cout << unterimOrder << "    " << resultOrder << endl;
  if (!hasPoint) resultOrder += resultMantissa.size()-1;
  else if (unterimOrder == 0) resultOrder--;
  else if (unterimOrder > 0)
  {
    if (resultOrder - unterimOrder + 1 >= -99999 && resultOrder - unterimOrder + 1 <= 99999)
      resultOrder -= unterimOrder + 1;
    else
    {
      resultMantissa.insert(resultMantissa.begin(), 0);
      resultMantissa.pop_back();
      cout << "Unable to normalize the mantissa due to order overflow..." << endl;
    }
  }
  else if (unterimOrder < 0)
  {
    if (resultOrder - unterimOrder + 1 >= -99999 && resultOrder - unterimOrder + 1 <= 99999)
      resultOrder -= unterimOrder + 1;
    else
    {
      resultMantissa.insert(resultMantissa.begin(), 0);
      resultMantissa.pop_back();
      cout << "Unable to normalize the mantissa due to order overflow..." << endl;
    }
  }
  resultMantissa = round(resultMantissa);
  if ((resultMantissa.size() == 1 && resultMantissa[0] == 0) || resultMantissa.size() == 0)
  {
    resultOrder = 0;
    resultMantissa.push_back(0);
  }
  if (resultOrder > 99999 || resultOrder < -99999)
  {
    cout << "Order overflow.\nQuitting..." << endl;
    exit(-1);
  }
  result.mantissa = resultMantissa;
  result.mantissaSign = resultMantissaSign;
  result.order = resultOrder;
  return result;
}

vector<short> round(vector<short> v)
{
  if (v.size() < 31) return v;
  if (v[v.size()-1] == v[v.size()-2] && v[v.size()-1] >= 5 && v[v.size()-1] < 9)
    v[v.size()-2]++;
  else if ((v[v.size()-1] == v[v.size()-2] && v[v.size()-1] == 9))
  {
    for (vector<short>::iterator iter = v.end()-1; iter != v.begin()-1; iter--)
    {
      if (*iter == 9) v.pop_back();
      else
      {
        (*iter)+=1;
        break;
      }
    }
  }
  else if (v[v.size() - 1] >= 5 && v[v.size()-2] < 9)
    v[v.size()-1]++;
  else if (v[v.size() - 1] >= 5 && v[v.size() - 2] == 9)
    {
      v.pop_back();
      for (vector<short>::iterator iter = v.end()-1; iter != v.begin() - 1
           ; iter--)
        {
          if (*iter == 9) v.pop_back();
          else
          {
            (*iter)+=1;
            break;
          }
        }
    }
  if (v.size() == 31) v.pop_back();
  v = deleteZeros(v);
  return v;
}

vector<short> divideMantissas(vector<short> dividentMantissa, vector<short> dividerMantissa, long long int *ptrOrder, bool* ptrHasPoint)
{
  /* Делит мантиссы */
  vector<short> result;
  bool hasPoint = false;
  int pointPosition = 0;
  bool hasOnlyZeros = true;
  result.push_back(0);
  while ((!isZero(dividentMantissa) || dividentMantissa.size() != 0) && result.size() <= 30)
  {
    if (isFirstGreater(dividerMantissa, dividentMantissa) && hasPoint)
    {
      dividentMantissa.push_back(0);
      result.push_back(0);
    }
    if (isFirstGreater(dividerMantissa, dividentMantissa) && !isEqual(dividerMantissa, dividentMantissa) && !hasPoint)
    {
      hasPoint = true;
      if (result[0] != 0) pointPosition = -result.size();
      else pointPosition = 0;
      if (*result.begin() != 0 && !hasOnlyZeros) {dividentMantissa.push_back(0); result.push_back(0);}
      //else if (*result.begin() == 0 && hasOnlyZeros) pointPosition++;
      if (result[result.size()-1] != 0) result.push_back(0);
    }

    size_t originalLen = dividerMantissa.size();
    while (dividerMantissa.size() != dividentMantissa.size() && !hasPoint)
    {
      dividerMantissa.push_back(0);
    }
    while (dividerMantissa.size() >= originalLen && isFirstGreater(dividentMantissa, dividerMantissa))
    {
      while (isFirstGreater(dividentMantissa, dividerMantissa))
      {
        hasOnlyZeros = false;
        dividentMantissa = subtractNumericalStrings(dividentMantissa, dividerMantissa);
        dividentMantissa = deleteStartZeros(dividentMantissa);
        result[result.size()-1]++;
      }
      if (dividerMantissa.size() == originalLen) break;
      result.push_back(0);
      if (dividerMantissa.size() != originalLen)
        dividerMantissa.pop_back();
    }
    if(*result.begin()==0 && hasOnlyZeros && hasPoint)
    {
      result.erase(result.begin());
      pointPosition++;
    }
  }
  if (pointPosition > 0)
    pointPosition--;
  if (hasPoint)
  {
    *ptrHasPoint = true;
    if (pointPosition == 0)
      *ptrOrder = 0;
    if ( pointPosition != 0)
      *ptrOrder = pointPosition;
  }
  result = deleteZeros(result);
  return result;
}

vector<short> deleteZeros(vector<short> v)
{
  size_t i = v.size() - 1;
  while (i >= 0)
  {
    if (v[i] == 0) v.pop_back();
    else break;
    i--;
  }
  return v;
}

vector<short> deleteStartZeros(vector<short> vec)
{
  /* Уадаляет нули в начале вектора */
  vector<short> result;
  size_t start = 0;
  for (size_t i = 0; i < vec.size(); i++)
  {
    if (vec[i] == 0) start = i+1;
    if (vec[i] != 0) break;
  }
  if (start != 0)
  {
    for (size_t i = start; i < vec.size(); i++)
      result.push_back(vec[i]);
  }
  else result = vec;
  return result;
}

vector<short> subtractNumericalStrings(vector<short> minuend, vector<short> subtrahend)
{
  /* Вычитание только положительных чисел, уменьшаемое обязательно больше или равно вычитаемому */
  vector<short> result;

  size_t minuendSize = minuend.size() - 1;
  size_t subSize = subtrahend.size() - 1;
  short currentMinItem;
  short currentSubItem;
  bool flag = true;
  bool flagEndSub = true;
  bool f = true;
  while (flag)
  {
    if (minuendSize == 0) flag = false;
    if (subSize == 0) flagEndSub = false;

    currentMinItem = minuend[minuendSize];
    (f) ? currentSubItem = subtrahend[subSize] : currentSubItem = 0;

    if (currentMinItem - currentSubItem < 0)
    {
      currentMinItem += 10;
      minuend[minuendSize-1]--;
    }
    minuendSize--;
    if (subSize != 0) subSize--;
    result.insert(result.begin(), currentMinItem - currentSubItem);
    if (minuend[0] == 0) flag = false;
    if (!flagEndSub) f = false;
  }
  return result;
}

vector<short> add(vector<short> vec, short num)
{
  /* Прибавляет num к вектору, считая вектор обычным числом */
  vector<short> add;

  if (vec.size() == 30 && isBiggest(vec))
  {
    for (unsigned int i = 0; i <= 30; i++)
    {
      i == 0 ? vec[i] = 1 : vec[i] = 0;
    }
  }
  else
    if (vec.size() != 0) vec.back() += num;
    else vec.push_back(num);
  return vec;
}

bool isBiggest(vector<short> vec)
{
  /* Проверяет, содержит ли число только девятки */
  bool res = true;
  for (unsigned int i = 0; i < vec.size() - 1; i++)
  {
    if (vec[i] != 9)
    {
      res = false;
      break;
    }
  }
  return  res;
}

bool isEqual(vector<short> num1, vector<short> num2)
{
  if (num1.size() != num2.size())
  {
      return false;
  }
  for (size_t i = 0; i < num1.size(); i++)
  {
    if (num1[i] != num2[i]) return  false;
  }
  return true;
}

bool isFirstGreater(vector<short> num1, vector<short> num2)
{
  /* Сравнение чисел, записанных в вектор
     Возвращает true, если первое больше или равно второму, иначе false */
  if (num1.size() != num2.size())
  {
      return (num1.size() >= num2.size()) ? true : false;
  }
  for (size_t i = 0; i < num1.size(); i++)
  {
    if (num1[i] < num2[i] && i == 0) return false;
    if (num1[i] > num2[i] && i == 0) return true;
    if (num1[i] < num2[i] && i != 0) return false;
    if (num1[i] > num2[i] && i != 0) return true;
  }
  return true;
}

void handleMantissas(string* divident, string* divider)
{
  /* Удаляет точки из мантисс */
  bool hasPointDivident = hasPoint(*divident);
  bool hasPointDivider = hasPoint(*divider);
  if (hasPointDivident | hasPointDivider)
  {
    unsigned int dividentPointPosition;
    unsigned int dividerPointPosition;
    unsigned int dividentNumsAfterPoint = 0;
    unsigned int dividerNumsAfterPoint = 0;
    dividentPointPosition = hasPointDivident ? (*divident).find(".") : 0;
    dividerPointPosition = hasPointDivider ? (*divider).find(".") : 0;
    if (hasPointDivident) dividentNumsAfterPoint = (*divident).size() - dividentPointPosition - 1;
    if (hasPointDivider) dividerNumsAfterPoint = (*divider).size() - dividerPointPosition - 1;

    if (dividentNumsAfterPoint > dividerNumsAfterPoint)
    {
      *divider += string(stringByNumber("0", (dividentNumsAfterPoint-dividerNumsAfterPoint)));
      //*divider += string(MyString("0")*(dividentNumsAfterPoint-dividerNumsAfterPoint));
    }
    else if (dividentNumsAfterPoint < dividerNumsAfterPoint)
    {
      //*divident += string(MyString("0")*(dividerNumsAfterPoint-dividentNumsAfterPoint));
      *divider += string(stringByNumber("0", (dividerNumsAfterPoint-dividentNumsAfterPoint)));
    }
    if (hasPointDivident) (*divident).replace(dividentPointPosition, 1, "");
    if (hasPointDivider) (*divider).replace(dividerPointPosition, 1, "");
  }
}

string stringByNumber(string s, size_t n)
{
  string result = s;
  if (n > 1)
  {
      for (size_t i = 1; i < n; i++)
      {
        result += s;
      }
  }
  return result;
}

string deleteInsignificantZeros(const string s)
{
  /* Удаляет нули в начале строки */
  string copy = s;
  size_t size = s.size();
  for (size_t i = 0; i < size; i++)
  {
    if (copy[i] == '0')
    {
      copy.replace(i, 1, "");
      size--;
      i--;
    }
    else break;
  }
  return copy;
}

bool isZero(vector<short> num)
{
  /* Возвращает true, если в num нет отличных от нуля чисел, иначе false */
  for (size_t i = 0; i < num.size(); i++)
  {
    if (num[i] != 0 && num[i] != '.')
      return false;
  }
  return true;
}

bool hasPoint(string s)
{
  /* Проверяет, есть ли в строке символ точка */
  for (size_t i = 0; i < s.size(); i++)
  {
    if (s[i] == '.') return true;
  }
  return false;
}

vector<short> convertMantissaToVector(string mantissa)
{
  /* Переписывает мантиссу из строки в вектор */
  vector<short> result;
  for (size_t i = 0; i < mantissa.size(); i++) result.push_back(mantissa[i] & 0x0F);
  return result;
}

void inputMember(string* mantissa, string* order, string message)
{
  /* Ввод и проверка всех исходных данных */
  cout << message << endl;
  cout << "                   |0        |10       |20       |" << endl;
  cout << "    Input mantissa: ";
  cin  >> *mantissa;
  switch (checkMantissa(*mantissa))
  {
    case TOO_BIG_MANTISSA:
      cout << "    Too big mantissa.\nQuitting..." << endl;
      exit(-1);
    case WRONG_SYMBOL:
      cout << "    Wrong symbol.\nQuitting..." << endl;
      exit(-1);
  }
  cout << "    Input order: ";
  cin >> *order;
  switch (checkOrder(*order))
  {
    case TOO_BIG_ORDER:
      cout << "    Too big order.\nQuitting..." << endl;
      exit(-1);
    case TOO_SMALL_ORDER:
      cout << "    Too small order.\nQuitting..." <<endl;
      exit(-1);
    case WRONG_SYMBOL:
      cout << "    Wrong symbol.\nQuitting..." << endl;
      exit(-1);
  }
}

void printHead()
{
  /* Печать информации о программе */
  cout << "Program for dividing a real number by a real number" << endl;
  cout << "Mantissa must contain 30 or less numbers" << endl;
  cout << "Order must be less than 99999 and more than -99999" << endl;
  cout << "Don`t use '+' for positive numbers" << endl;
  cout << "Don't use exponential numbaes\n" << endl;
}

int checkOrder(string order)
{
  /* Проверяет правильность ввода порядка */
  if (order == "-100000") return TOO_SMALL_ORDER;
  if (order == "100000") return TOO_BIG_ORDER;
  if (order.size() == 1 && order[0] == '-') return WRONG_SYMBOL;

  bool isNegative = (order[0] == '-') ? true : false;
  for (size_t i = isNegative ? 1 : 0; i < order.size(); i++)
  {
    if (!isdigit(order[i])) return WRONG_SYMBOL;
  }
  if (!isNegative && order.size() > 5) return TOO_BIG_ORDER;
  if (isNegative && order.size() > 6) return TOO_SMALL_ORDER;
  return 0;
}

int checkMantissa(string mantissa)
{
  /* Проверяет правильность ввода мантиссы */
  if (mantissa.size() > 32)
    return TOO_BIG_MANTISSA;
  bool hasDot = false;
  if (mantissa.size() == 1 && mantissa[0] == '-') return WRONG_SYMBOL;
  bool isNegative = (mantissa[0] == '-') ? true : false;
  for (size_t i = isNegative ? 1 : 0; i < mantissa.size(); i++)
  {
    if (!isdigit(mantissa[i]))
    {
      if (mantissa[i] == '.')
      {
        if (hasDot == true) { return WRONG_SYMBOL; }
        else { hasDot = true; continue; }
      }
      return WRONG_SYMBOL;
    }
  }
  if (hasDot && isNegative && mantissa.size() > 32) return TOO_BIG_MANTISSA;
  if (hasDot && !isNegative && mantissa.size() > 31) return TOO_BIG_MANTISSA;
  if (!hasDot && isNegative && mantissa.size() > 31) return TOO_BIG_MANTISSA;
  if (!hasDot && ! isNegative && mantissa.size() > 30) return TOO_BIG_MANTISSA;
  return 0;
}
