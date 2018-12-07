#ifndef SPARSEMATRIX_H
#define SPARSEMATRIX_H

#include <iostream>
#include <vector>
#include "firstincolumn.h"
#include "matrix.h"

using namespace std;

struct Item
{
    size_t column;
    size_t row;
    double value;
};

struct SparseMatrix
{
private:
    size_t mRows;
    size_t mColumns;
    vector<double> mValues;
    vector<size_t> mRowIndex;
    vector<FirstColumn> mFirstInColumn;
public:
    SparseMatrix operator+(const SparseMatrix* matrix);
    SparseMatrix(vector<double> values, vector<size_t> rowIndex, vector<FirstColumn> firstInRow, size_t rows, size_t columns);
    SparseMatrix();
    vector<double> values() const;
    void setValues(const vector<double> &values);
    size_t rows() const;
    void setRows(const size_t &rows);
    size_t columns() const;
    void setColumns(const size_t &columns);
    vector<size_t> rowIndex() const;
    void setRowIndex(const vector<size_t> &rowIndex);
    vector<FirstColumn> firstInColumn() const;
    void setFirstInColumn(vector<FirstColumn> firstInColumn);
    void outSparseMatrix();
    Matrix* toMatrix();
    bool isNotZeroElem(size_t row, size_t column, vector<size_t> columns, vector<size_t> rows);
    static SparseMatrix* initSparseMatrix( vector<Item>* items, size_t rowsCount, size_t columnsCount);
    static void sorter(vector<Item> *items);
    double getElem(size_t row, size_t col, vector<size_t> columns) const;
};

#endif // SPARSEMATRIX_H
