#ifndef STATICSTACK_H
#define STATICSTACK_H

#include "absractcontainer.h"

template <typename Type>
class StaticStack : public AbstractContainer<Type> // Наследование
{
  typedef AbstractContainer<Type> Base;
  Type* mElements;
public:

  unsigned long getBytesSize()
  {
      return  sizeof (Type) * this->getSizeElement() + sizeof (AbstractContainer<Type>);
  }

  StaticStack(uint64_t size) : AbstractContainer<Type>(size)
  {
      mElements = new Type[size];
  }

  ~StaticStack() {
    delete [] mElements;
  }

  virtual void push(Type value) override
  {
    if (Base::getTopValue() == Base::getSizeElement()) throw std::bad_exception();
    mElements[Base::getTopValue()] = value;
    Base::elementAdd();
  }

  virtual void clean() override
  {
      for (uint32_t timeTopPtr = Base::getTopValue(); timeTopPtr > 0; --timeTopPtr)
          pop();
  }

  virtual Type pop() override
  {
    if (this->getSizeElement() == 0)
        throw std::bad_exception();
    Base::elementBack();
    Type t = mElements[Base::getTopValue()];
//    mElements[Base::getTopValue()] = 0;
    return t;
  }

  virtual void print() override
  {
    if (this->getSizeElement() == 0)
        std::cout << "Стек пустой" << std::endl;
    for (uint32_t timeTopPtr = Base::getTopValue(); timeTopPtr > 0; --timeTopPtr)
        std::cout << "Element # " << timeTopPtr << " : " << pop() << std::endl;
  }

  void printNoDelete()
  {
      if (this->getSizeElement() == 0)
          std::cout << "Стек пустой" << std::endl;
      for (uint32_t timeTopPtr = Base::getTopValue(); timeTopPtr > 0; --timeTopPtr)
          std::cout << "Element # " << timeTopPtr << " : " << mElements[timeTopPtr - 1] << std::endl;
  }
};


#endif // STATICSTACK_H
