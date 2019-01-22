#include "myreal.h"
#include <stdlib.h>
#include <cmath>
#include "mystring.h"
#include <string.h>
#include <vector>

using std::string;

MyReal::MyReal(string mantissa, long long int order, short mantSign)
{
  mMantissa = mantissa;
  mOrder = order;
  mMantSign = mantSign;
}

//std::vector<int> subtractNumericalStrings(std::vector<int> minuend, std::vector<int> subtrahend)
//{
//  /* Вычитание только положительных чисел, уменьшаемое обязательно больше или равно вычитаемому */
//  std::vector<int> result;

//  size_t minuendSize = minuend.size() - 1;
//  size_t subSize = subtrahend.size() - 1;
//  int currentMinItem;
//  int currentSubItem;
//  bool flag = true;
//  short flagEndSub = 0;
//  while (flag)
//  {
//    if (minuendSize == 0) flag = false;

//    currentMinItem = minuend[minuendSize];
//    (flagEndSub != 1) ? currentSubItem = subtrahend[subSize] : currentSubItem = 0;

//    if (currentMinItem - currentSubItem < 0)
//    {
//      currentMinItem += 10;
//      minuend[minuendSize-1]--;
//    }
//    minuendSize--;
//    if (subSize != 0) subSize--;
//    if (subSize == 0 && flagEndSub == 1) flagEndSub = 2;
//    else if ((subSize == 0 && flagEndSub == 0) || (subSize == 0 && flagEndSub == 0 && minuendSize == 0)) flagEndSub = 1;
//    result.insert(result.begin(), currentMinItem - currentSubItem);
//    if (minuend[0] == 0) flag = false;
//  }
//  return result;
//}


MyReal MyReal::operator / (MyReal divider)
{
  /* Проверка, является ли делитель нулем */
  try {
    if (isZero(divider.getMantissa())) throw (0);
  } catch (int) {
    std::cout << "Dividing by zero.\nQuitting..." << std::endl;
    exit(-1);
  }

  /* Проверка на переполнение порядка в результате деления */
  long long int resultOrder = mOrder - divider.getOrder();
  if (resultOrder >= 99999 || resultOrder <= -99999)
  {
    std::cout << "Order overflow.\nQuitting..." << std::endl;
    exit(-1);
  }

  string resultMantissa;
  short resultMantSign;

  resultMantissa = divideMantissas(mMantissa, divider.getMantissa());

  std::cout << "Result mantissa conuted." << std::endl;
  resultMantSign = mMantSign * divider.getMantissaSign();

  std::cout << "Finish." << std::endl;
  MyReal result = MyReal(resultMantissa, resultOrder, resultMantSign);
  return result;
}


bool MyReal::isFirstGreater(std::vector<int> num1, std::vector<int> num2)
{
  /* Сравнение чисел, записанных в вектор
     Возвращает true, если первое больше второго, иначе false */
  if (num1.size() != num2.size())
  {
      return (num1.size() >= num2.size()) ? true : false;
  }
  for (size_t i = 0; i < num1.size(); i++)
  {
    if (num1[i] < num2[i]) return false;
  }
  return true;
}

std::vector<int> MyReal::subtractNumericalStrings(std::vector<int> minuend, std::vector<int> subtrahend)
{
  /* Вычитание только положительных чисел, уменьшаемое обязательно больше или равно вычитаемому */
  std::vector<int> result;

  size_t minuendSize = minuend.size() - 1;
  size_t subSize = subtrahend.size() - 1;
  int currentMinItem;
  int currentSubItem;
  bool flag = true;
  bool flagEndSub = false;
  while (flag)
  {
    if (minuendSize == 0) flag = false;

    currentMinItem = minuend[minuendSize];
    (!flagEndSub) ? currentSubItem = subtrahend[subSize] : currentSubItem = 0;

    if (currentMinItem - currentSubItem < 0)
    {
      currentMinItem += 10;
      minuend[minuendSize-1]--;
    }
    minuendSize--;
    if (subSize != 0) subSize--;
    if (subSize == 0) flagEndSub = true;
    std::cout << currentMinItem - currentSubItem << std::endl;
    result.insert(result.begin(), currentMinItem - currentSubItem);
    if (minuend[0] == 0) flag = false;
  }
  return result;
}


string MyReal::deleteInsignificantZeros(const string s)
{
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

bool MyReal::hasPoint(string s)
{
  for (size_t i = 0; i < s.size(); i++)
  {
    if (s[i] == '.') return true;
  }
  return false;
}


string MyReal::divideMantissas(string divident, string divider)
{
  string result;
  int wholes = 0;

  std::cout << divident << std::endl;
  std::cout << divider << std::endl;

  bool hasPointDivident = hasPoint(divident);
  bool hasPointDivider = hasPoint(divider);


  if (hasPointDivident | hasPointDivider)
  {
    unsigned int dividentPointPosition;
    unsigned int dividerPointPosition;
    unsigned int dividentNumsAfterPoint = 0;
    unsigned int dividerNumsAfterPoint = 0;

    dividentPointPosition = hasPointDivident ? divident.find(".") : 0;
    dividerPointPosition = hasPointDivider ? divider.find(".") : 0;

    if (hasPointDivident) dividentNumsAfterPoint = divident.size() - dividentPointPosition - 1;
    if (hasPointDivider) dividerNumsAfterPoint = divider.size() - dividerPointPosition - 1;

    if (dividentNumsAfterPoint > dividerNumsAfterPoint)
    {
      divider += string(MyString("0")*(dividentNumsAfterPoint-dividerNumsAfterPoint));
    }
    else if (dividentNumsAfterPoint < dividerNumsAfterPoint)
    {
      divident += string(MyString("0")*(dividerNumsAfterPoint-dividentNumsAfterPoint));
    }

    if (hasPointDivident) divident.replace(dividentPointPosition, 1, "");
    if (hasPointDivider) divider.replace(dividerPointPosition, 1, "");
  }

  divident = deleteInsignificantZeros(divident);
  divider = deleteInsignificantZeros(divider);

  std::vector<int> dntMantissa;
  std::vector<int> drMantissa;

  for (size_t i = 0; i < divident.size(); i++) dntMantissa.push_back(mMantissa[i] & 0x0F);
  for (size_t i = 0; i < divider.size(); i++) drMantissa.push_back(divider[i] & 0x0F);

  if (isFirstGreater(dntMantissa, drMantissa)) std::cout << "true" << std::endl;
  else std::cout << "false" << std::endl;
  while (isFirstGreater(dntMantissa, drMantissa))
  {
    dntMantissa = subtractNumericalStrings(dntMantissa, drMantissa);
    wholes++;
  }

  std::cout << wholes << std::endl;

//  char buff[1];
//  result += itoa(wholes, buff, 10);
//  result += ".";
//  wholes = 0;
//  while (result.size() - 1 < 32)
//  {
//    if (!isZero(divident))
//    {
//      divident += "0";
//      result += "0";
//      while (isFirstGreater(divident, divider))
//      {
//        divident = subtractNumericalStrings(divident, divider);
//        wholes++;
//      }
//      char buff[1];
//      result += itoa(wholes, buff, 10);
//    }
//  }
  return result;
}


bool MyReal::isZero(string num)
{
  /* Возвращает true, если в num нет отличных от нуля чисел, иначе false */
  bool isNegative = (num[0] == '-') ? true : false;
  for (size_t i = isNegative ? 1 : 0; i < num.size(); i++)
  {
    if (num[i] != '0' && num[i] != '.')
      return false;
  }
  return true;
}


//vector<int> divideMantissas(vector<int> dividentMantissa, vector<int> dividerMantissa)
//{
//  vector<int> result;
//  while (isFirstGreater(dividentMantissa, dividerMantissa))
//  {
//    dividentMantissa = subtractNumericalStrings(dividentMantissa, dividerMantissa);
//    result = add(result, 1);

//  }

//  if (!isZero(dividentMantissa)) dividentMantissa.push_back(0);

//  vector<int> resAfterPoint;

//  while (!isZero(dividentMantissa) && result.size() + resAfterPoint.size() < 30)
//  {
//    if (isFirstGreater(dividerMantissa, dividentMantissa))
//    {
//      resAfterPoint.push_back(0);
//      dividentMantissa.push_back(0);
//    }
//    while (isFirstGreater(dividentMantissa, dividerMantissa))
//    {
//      dividentMantissa = subtractNumericalStrings(dividentMantissa, dividerMantissa);
//      resAfterPoint = add(resAfterPoint, 1);
//    }
//  }

//  for (unsigned int i = 0; i < resAfterPoint.size(); i++)
//    {
//      cout << resAfterPoint[i];
//    }
////  while (result.size() <= 29 || !isZero(dividentMantissa))
////  {
////    if (!isFirstGreater(dividentMantissa, dividerMantissa))
////    {
////      result.push_back(0);
////      dividentMantissa.push_back(0);
////    }
////  }


//  return result;
//}

