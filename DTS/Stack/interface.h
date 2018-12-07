#ifndef INTERFACE_H
#define INTERFACE_H

#include <iostream>

class Interface
{
public:
    Interface(){}
    virtual void print(size_t idx) = 0;
};

#endif // INTERFACE_H
