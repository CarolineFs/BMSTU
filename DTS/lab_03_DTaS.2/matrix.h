#ifndef MATRIX_H
#define MATRIX_H
#include <iostream>

using namespace std;

struct Matrix
{
private:
    size_t mRows;
    size_t mColumns;
public:
    double** mValues;
    Matrix* operator+(const Matrix* matrix);
    Matrix(size_t rows, size_t columns, double** values);
    Matrix(size_t rows, size_t columns);
    Matrix();
    ~Matrix();
    size_t rows() const;
    void setRows(const size_t &rows);
    size_t columns() const;
    void setColumns(const size_t &columns);
    double **values() const;
    void setValues(double **values);
    void outMatrix();
};

#endif // MATRIX_H
