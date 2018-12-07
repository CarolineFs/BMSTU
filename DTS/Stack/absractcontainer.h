#ifndef STACK_H
#define STACK_H

#include <stdint.h>
#include <exception>
#include <string>
#include <iostream>
#include <sstream>

// Абстрактный класс
template <typename Type>
class AbstractContainer
{
  uint64_t mSizeContainer; // Размер контейнера
  uint32_t mTopPtr;        // Верхний индекс
public:
  AbstractContainer(uint64_t size = 0) : mSizeContainer(size), mTopPtr(0){}
  virtual ~AbstractContainer() {}
// Общий интерфейс
  virtual void push(Type value) = 0; // Абстрактный метод virtual = 0
  virtual Type pop()            = 0;
  virtual void print()          = 0;
  virtual void clean()          = 0;
//------------------------
protected:
  virtual void setTopPtr(const uint32_t &topPtr) { mTopPtr = topPtr; }
  virtual uint64_t getSizeElement() const { return mSizeContainer; }
  virtual uint32_t getTopValue() const { return mTopPtr; }
  void elementAdd() { mTopPtr += 1; }
  void elementBack()
  {
    if(mTopPtr != 0) mTopPtr -= 1;
    else throw std::bad_exception();
  }
};

#endif // STACK_H
