#ifndef FUNCTOR_H
#define FUNCTOR_H

#include "sparsematrix.h"

//Функтор сортировки по колонке
struct SorterByColumn
{
    bool operator()(const Item& a, const Item& b) const
    {
        return a.column < b.column;
    }

};

//Функтор сортировки по строкам
struct SorterByRow
{
    bool operator()(const Item& a, const Item& b) const
    {
        return a.row < b.row;
    }

};
#endif // FUNCTOR_H
