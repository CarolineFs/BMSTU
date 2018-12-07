#include "firstincolumn.h"

FirstColumn::FirstColumn()
  : mPosition(pair<size_t, size_t>(0, 0))
{

}

pair<size_t, size_t> FirstColumn::getPosition() const
{
    return mPosition;
}

void FirstColumn::setPosition(const pair<size_t, size_t> &position)
{
    mPosition = position;
}

size_t FirstColumn::getIdx() const
{
    return idx;
}

void FirstColumn::setIdx(const size_t &value)
{
    idx = value;
}

//FirstColumn *FirstColumn::getNext() const
//{
//    return next;
//}

//void FirstColumn::setNext(FirstColumn *value)
//{
//    next = value;
//}
