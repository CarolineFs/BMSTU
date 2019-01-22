#pragma once
#include <string>

using std::string;

class MyString
{
  string mInnerValue;
public:
  MyString(const char*);
  MyString(string val);
  string operator*(const unsigned int& num);
  string operator-(const string&);
  bool isEmpty();

};

