#include "mystring.h"

MyString::MyString(const char * ch)
{
  mInnerValue = ch;
}

MyString::MyString(string val)
{

  mInnerValue = val;
}

std::string MyString::operator*(const unsigned int &num)
{
  string buffer = mInnerValue;
  if (num > 1)
  {
      for (size_t i = 1; i < num; i++)
      {
        mInnerValue += buffer;
      }
  }
  return mInnerValue;

}

bool MyString::isEmpty()
{
  return mInnerValue.empty();
}

