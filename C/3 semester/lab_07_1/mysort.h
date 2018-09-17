#ifndef MYSORT_H
#define MYSORT_H
#include <stdio.h>

void mySort( void * first, size_t number, size_t size, int ( * comparator ) ( const void *, const void * ) );

#endif // MYSORT_H
