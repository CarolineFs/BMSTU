#ifndef DYNAMICSTACK_H
#define DYNAMICSTACK_H

#include "absractcontainer.h"
#include <vector>

template <typename Type>
class DynamicStack : public AbstractContainer<Type>
{
  typedef AbstractContainer<Type> Base;
  struct Item
  {
    Item():downerItem(nullptr){}
    Type value;
    Item* downerItem;
  };
  Item* ptrTopItem;
  Item* ptrEndItem;
public:

  unsigned long getBytesSize()
  {
      return sizeof(AbstractContainer<Type>) + sizeof (Item) + sizeof (Item) * this->getTopValue();
  }

  enum Mode { ADDRESS, VALUE };
  enum Dropped { NONE, POP };

  DynamicStack() : Base(), ptrTopItem(nullptr), ptrEndItem(nullptr){}
  virtual ~DynamicStack()
  {
      clean();
  }

  virtual void push(Type value) override
  {
    if (ptrTopItem == nullptr)
      {
        ptrTopItem = new Item;
        ptrEndItem = ptrTopItem;
      }
    else
      {
        Item* newElement = new Item;
        newElement->downerItem = ptrTopItem;
        ptrTopItem = newElement;
      }
    ptrTopItem->value = value;
    Base::elementAdd();     // Необязательный параметр
  }

  virtual Type pop() override
  {
    if (this->ptrTopItem == nullptr)
        throw std::bad_exception();
    Base::elementBack();    // Необязательный параметр
    Type value = ptrTopItem->value;
    Item* freeItem = ptrTopItem;
    ptrTopItem = ptrTopItem->downerItem;
    delete freeItem;
    std::cout << "Element # " << value << std::endl;
    std::cout << "Address # " << freeItem << std::endl;
    freeItem = nullptr;
    return value;
  }

  virtual void clean() override
  {
      Item* timePtr = ptrTopItem;
      while (timePtr != nullptr) {
          timePtr = timePtr->downerItem;
          pop();
        }
  }

  virtual void* popAddr()
  {
      Base::elementBack();    // Необязательный параметр
      Item* freeItem = ptrTopItem;
      ptrTopItem = ptrTopItem->downerItem;
      delete freeItem;
      return freeItem;
  }

  virtual void print() override
  {
    if (ptrTopItem == nullptr)
    {
        std::cout << "Стек пустой." << std::endl;
        return;
    }
    Item* timePtr = ptrTopItem;
    int counter = this->getTopValue();
    while (timePtr != nullptr) {
        std::cout << "Element # " << counter-- << " : " << pop() << std::endl;
        timePtr = timePtr->downerItem;
      }
  }

  virtual void printParam(Mode m, Dropped d = Dropped::NONE)
  {
//      Item* timePtr = ptrTopItem;
//      int counter = 0;
//      while (timePtr != nullptr) {
//          std::cout << "Element # " << ++counter << " : " << ((d == NONE) ? timePtr->value : pop()) << std::endl;
//          timePtr = timePtr->downerItem;
//      }
    if (ptrTopItem == nullptr)
        std::cout << "Стек пустой." << std::endl;

    Item* timePtr = ptrTopItem;
    int counter = this->getTopValue();
    switch (m) {
      case VALUE:
            while (timePtr != nullptr) {
                std::cout << "Element # " << counter-- << " : " << ((d == NONE) ? timePtr->value : pop()) << std::endl;
                timePtr = timePtr->downerItem;
          }
            break;
      case ADDRESS:
            while (timePtr != nullptr) {
                std::cout << "Element # " << counter << " : " << timePtr->value << std::endl;
                std::cout << "Address # " << counter-- << " : " << ((d == NONE) ? &timePtr->value : popAddr()) << std::endl;
                timePtr = timePtr->downerItem;
            }
          break;
    }
  }

};

#endif // DYNAMICSTACK_H
