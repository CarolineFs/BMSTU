#ifndef FIRSTINCOLUMN_H
#define FIRSTINCOLUMN_H

#include <iostream>
#include <vector>

using namespace std;

struct FirstColumn
{
private:
    pair<size_t, size_t> mPosition; // <row, column>
    size_t idx;
    //struct FirstColumn* next;
public:
    FirstColumn *getNext() const;
    void setNext(FirstColumn *value);

    FirstColumn();
    pair<size_t, size_t> getPosition() const;
    void setPosition(const pair<size_t, size_t> &position);

    size_t getIdx() const;
    void setIdx(const size_t &value);
};

#endif // FIRSTINCOLUMN_H
