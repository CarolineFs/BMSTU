#include "sparsematrix.h"
#include "myexceptions.h"
#include "functor.h"
#include <algorithm>

size_t SparseMatrix::rows() const
{
    return mRows;
}

void SparseMatrix::setRows(const size_t &rows)
{
    mRows = rows;
}

size_t SparseMatrix::columns() const
{
    return mColumns;
}

void SparseMatrix::setColumns(const size_t &columns)
{
    mColumns = columns;
}

vector<size_t> SparseMatrix::rowIndex() const
{
    return mRowIndex;
}

void SparseMatrix::setRowIndex(const vector<size_t> &rowIndex)
{
    mRowIndex = rowIndex;
}


vector<FirstColumn> SparseMatrix::firstInColumn() const
{
    return mFirstInColumn;
}

void SparseMatrix::setFirstInColumn(vector<FirstColumn> firstInColumn)
{
    mFirstInColumn = firstInColumn;
}

void SparseMatrix::outSparseMatrix()
{
    cout << "-----------------------------------" << endl;
    cout << "Разреженная матрица: " << endl;
    cout << "Массив ненулевых элементов" << endl;
    for (vector<double>::iterator iter = mValues.begin(); iter != mValues.end(); iter++)
        cout << *iter << "    ";
    cout << endl;
    cout << "Номера строк" << endl;
    for (vector<size_t>::iterator iter = mRowIndex.begin(); iter != mRowIndex.end(); iter++)
        cout << *iter << "    ";
    cout << endl;
    cout << "Связный список" << endl;
    for (vector<FirstColumn>::iterator iter = mFirstInColumn.begin(); iter != mFirstInColumn.end(); iter++)
        cout << "<" << (*iter).getPosition().first << ","
             << (*iter).getPosition().second << "> "
             << ((*iter).getIdx())
             << "\t";
    cout << endl;
    cout << "-----------------------------------" << endl << endl;
}

Matrix* SparseMatrix::toMatrix()
{
    Matrix* result = new Matrix(mRows, mColumns);
    size_t count = 0;
    vector<size_t> restoredCols;
    for (vector<FirstColumn>::iterator iter = mFirstInColumn.begin(); iter != mFirstInColumn.end(); ++iter)
    {
        size_t idx;
        if (iter == mFirstInColumn.end() - 1)
            idx = mRowIndex.size();
        else
            idx = (*(iter+1)).getIdx();
        size_t curCol = (*(iter)).getPosition().second;
        for (size_t i = count; i < idx; ++i)
        {
            restoredCols.push_back(curCol);
            count++;
        }
    }
    for (size_t i = 0; i < restoredCols.size(); ++i)
    {
        size_t curCol = restoredCols[i];
        size_t curRow = mRowIndex[i];
        result->mValues[curRow][curCol] = mValues[i];
    }

    return result;
}

bool SparseMatrix::isNotZeroElem(size_t row, size_t column, vector<size_t> columns, vector<size_t> rows)
{
    for (size_t i = 0; i < rows.size(); ++i)
        if (rows[i] == row && columns[i] == column)
            return true;
    return false;
}

/**
 \throws InvalidMatrixSizeException
 */
SparseMatrix SparseMatrix::operator+(const SparseMatrix *matrix)
{
    if (mRows != matrix->rows() || mColumns != matrix->columns())
        {
            throw InvalidMatrixSizeException();
        }
        vector<Item> items;
        vector<size_t> paramColumns;
        vector<size_t> mColumnsVec;

        vector<size_t> resulrCols;
        vector<size_t> resultRows;

        size_t count = 0;
        size_t curCol;

        for (size_t i = 0; i < matrix->firstInColumn().size(); ++i)
        {
            size_t idx;
            if (i == matrix->firstInColumn().size() - 1)
                idx = matrix->rowIndex().size();
            else
                idx = matrix->firstInColumn()[i + 1].getIdx();
            curCol = matrix->firstInColumn()[i].getPosition().second;
            for (size_t i = count; i < idx; ++i)
            {
                paramColumns.push_back(curCol);
                count++;
            }
        }

        count = 0;
        for (size_t i = 0; i < mFirstInColumn.size(); ++i)
        {
            size_t idx;
            if (i == mFirstInColumn.size() - 1)
                idx = mRowIndex.size();
            else
                idx = mFirstInColumn[i+1].getIdx();
            size_t curCol = mFirstInColumn[i].getPosition().second;
            for (size_t i = count; i < idx; ++i)
            {
                mColumnsVec.push_back(curCol);
                count++;
            }
        }
//        for (vector<FirstColumn>::iterator iter = matrix->firstInColumn().begin(); iter < matrix->firstInColumn().end(); ++iter)
//        {
//            size_t idx;
//            if (iter == matrix->firstInColumn().end() - 1)
//                idx = matrix->rowIndex().size();
//            else
//                idx = (*(iter+1)).getIdx();
//            curCol = (*(iter)).getPosition().second;
//            for (size_t i = count; i < idx; ++i)
//            {
//                paramColumns.push_back(curCol);
//                count++;
//            }
//            int a = 0;
//        }

//        count = 1;
//        mColumnsVec.push_back(mFirstInColumn.at(0).getPosition().second);
//        for (vector<FirstColumn>::iterator iter = mFirstInColumn.begin(); iter < mFirstInColumn.end(); ++iter)
//        {
//            size_t idx;
//            if (iter == mFirstInColumn.end() - 1)
//                idx = mRowIndex.size();
//            else
//                idx = (*(iter+1)).getIdx();
//            size_t curCol = (*(iter)).getPosition().second;
//            for (size_t i = count; i < idx; ++i)
//            {
//                mColumnsVec.push_back(curCol);
//                count++;
//            }
//        }

        for (size_t i = 0; i < matrix->rowIndex().size(); ++i)
        {
            resultRows.push_back(matrix->rowIndex().at(i));
            resulrCols.push_back(paramColumns.at(i));
        }

        for (size_t i = 0; i < mRowIndex.size(); ++i)
        {
            size_t curRow = mRowIndex.at(i);
            size_t curCol = mColumnsVec.at(i);
            if (!isNotZeroElem(curRow, curCol, resulrCols, resultRows))
            {
                resultRows.push_back(curRow);
                resulrCols.push_back(curCol);
            }
        }
        for (size_t i = 0; i < resultRows.size(); ++i)
        {
            size_t curRow = resultRows[i];
            size_t curCol = resulrCols[i];
            Item item;
            item.row = curRow;
            item.column = curCol;
            double elem1 = this->getElem(curRow, curCol, mColumnsVec);
            double elem2 = matrix->getElem(curRow, curCol, paramColumns);
            item.value = elem1 + elem2;
            items.push_back(item);
        }

//        SparseMatrix* res = initSparseMatrix(&items, mRows, mColumns);
//        res->outSparseMatrix();
        return *initSparseMatrix(&items, mRows, mColumns);
}


SparseMatrix::SparseMatrix(vector<double> values, vector<size_t> rowIndex, vector<FirstColumn> firstInColumn, size_t rows, size_t columns)
{
    mValues = values;
    mRowIndex = rowIndex;
    mFirstInColumn = firstInColumn;
    mRows = rows;
    mColumns = columns;
}

SparseMatrix::SparseMatrix()
{

}
vector<double> SparseMatrix::values() const
{
    return mValues;
}

void SparseMatrix::setValues(const vector<double> &values)
{
    mValues = values;
}

//Создание разреженной матрицы
SparseMatrix* SparseMatrix::initSparseMatrix( vector<Item>* items, size_t rowsCount, size_t columnsCount)
{
    std::sort(items->begin(), items->end(), SorterByColumn());
    sorter(items);
    SparseMatrix* matrix = new SparseMatrix();
    vector<size_t> rowIndex;
    vector<double>* values = new vector<double>();
    vector<FirstColumn> firstInColumn;

//    vector<size_t> indexesValue;

    size_t curItem = (*items->begin()).column;

    for (size_t i = 0; i < items->size(); ++i)
    {
        rowIndex.push_back(items->at(i).row);
        values->push_back(items->at(i).value);
        if (curItem != items->at(i).column || i == 0)
        {
            curItem = items->at(i).column;
            FirstColumn curFirstInColumn;
            curFirstInColumn.setPosition(pair<size_t, size_t> (items->at(i).row, items->at(i).column));
//            curFirstInColumn.setValuesPtr(values.begin()+i);
            curFirstInColumn.setIdx(rowIndex.size() - 1);
            firstInColumn.push_back(curFirstInColumn);
//            indexesValue.push_back(i);
//            firstInColumn[index++].setValuesPtr(&values[i]);
        }
    }



    matrix->setColumns(columnsCount);
    matrix->setRows(rowsCount);
    matrix->setRowIndex(rowIndex);
    matrix->setFirstInColumn(firstInColumn);
    matrix->setValues(*values);
    return matrix;
}


//Сортировка по строкам
void SparseMatrix::sorter(vector<Item>* items)
{
    size_t indent = 0; // отступ
    size_t count = 0; // Счетчик повторений
    size_t curValue = items->at(0).column;
    vector<FirstColumn> firstInColumn; // label
    for (size_t i = 0; i < items->size(); ++i)
    {
        if (curValue == items->at(i).column)
            count++;
        else
        {
            std::sort(items->begin() + indent, items->begin() + count + indent, SorterByRow());
            indent += count;
            curValue = items->at(i).column;
            count = 1;
        }
    }
    std::sort(items->begin() + indent, items->end(), SorterByRow());
}

double SparseMatrix::getElem(size_t row, size_t col, vector<size_t> columns) const
{
    double value = 0;
    for (size_t i = 0; i < mRowIndex.size(); ++i)
        if (mRowIndex[i] == row && columns[i] == col)
        {
            value = mValues[i];
            break;
        }
    return value;
}

