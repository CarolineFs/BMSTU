#pragma once
#include <string>
#include <cstring>
#include <iostream>
#include <sstream>
#include <vector>
using std::string;

class MyReal
{
private:
  string mMantissa;
  long long int mOrder;
  short mMantSign;
  string divideMantissas(string, string);
  bool isZero(string);
  bool isFirstGreater(std::vector<int>, std::vector<int>);
  std::vector<int> subtractNumericalStrings(std::vector<int>, std::vector<int>);
  string deleteInsignificantZeros(string);
  bool hasPoint(string);
  char getChar(string);
public:
  MyReal(string, long long int, short);
  string getMantissa() { return mMantissa; }
  long long int getOrder() { return mOrder; }
  short getMantissaSign() { return mMantSign; }
  MyReal operator / (MyReal divider);
};
