#ifndef DYNAMICQUEUE_H
#define DYNAMICQUEUE_H
#include "absractcontainer.h"

template <typename T>
class DynamicQueue : public AbstractContainer<T>
{
  typedef AbstractContainer<T> Base;
#pragma pack (push, 1)
  struct Item
  {
    T value;
    Item* nextItem;
  };
#pragma pack(pop)
  Item* mBeginPtr;
  Item* mEndPtr;
public:
  DynamicQueue() : Base(), mBeginPtr(nullptr) {}

  virtual void push(T value) override
  {
    if (mBeginPtr == nullptr)
      {
          mBeginPtr = new Item;
          mBeginPtr->nextItem = nullptr;
          mBeginPtr->value = value;
          mEndPtr = mBeginPtr;
      }
    else
      {
          mEndPtr->nextItem = new Item;
          mEndPtr = mEndPtr->nextItem;
          mEndPtr->value = value;
          mEndPtr->nextItem = nullptr;
      }
    Base::elementAdd();
  }

  virtual T pop() override
  {
    Base::elementBack();
    T val = mBeginPtr->value;
    Item* delPtr = mBeginPtr;
    mBeginPtr = mBeginPtr->nextItem;
    delete delPtr;
    delPtr = nullptr;
    return val;
  }

  virtual void print() override
  {
    Item* timePtr = mBeginPtr;
    uint32_t count = 0;
    while (timePtr != nullptr) {
        std::cout << "Element # " << ++count << " : " << timePtr->value << std::endl;
        timePtr = timePtr->nextItem;
      }
  }
};

#endif // DYNAMICQUEUE_H
