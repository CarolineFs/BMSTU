#ifndef STATICQUEUE_H
#define STATICQUEUE_H

#include "absractcontainer.h"

template <typename T>
class StaticQueue : public AbstractContainer<T>
{
  T* mElements;
  uint32_t totalSize = 0;
  typedef AbstractContainer<T> Base;
public:
  StaticQueue(uint64_t size) : AbstractContainer<T>(size)
  {
    mElements = new T[size];
  }

  virtual void push(T value) override
  {
    uint64_t curIndex = (Base::getTopValue() + totalSize) % Base::getSizeElement();
    totalSize != Base::getSizeElement() ? ++totalSize : throw std::bad_exception();
    mElements[curIndex] = value;
  }

  virtual T pop() override
  {
    totalSize != 0 ? --totalSize : throw std::bad_exception();
    T t = mElements[Base::getTopValue()];
//    mElements[Base::getTopValue()] = 0;

    Base::setTopPtr((Base::getTopValue() + 1) % Base::getSizeElement());
    return t;
  }

  virtual void print() override
  {
    for (uint32_t i = 0; i < totalSize; ++i)
      {
        uint32_t index = (i + Base::getTopValue()) % Base::getSizeElement();
        std::cout << "Element # " << i + 1 << " : " << mElements[index] << std::endl;
      }
  }
};

#endif // STATICQUEUE_H
