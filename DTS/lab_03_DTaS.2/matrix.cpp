#include "matrix.h"
#include "myexceptions.h"

size_t Matrix::rows() const
{
    return mRows;
}

void Matrix::setRows(const size_t &rows)
{
    mRows = rows;
}

size_t Matrix::columns() const
{
    return mColumns;
}

void Matrix::setColumns(const size_t &columns)
{
    mColumns = columns;
}

double **Matrix::values() const
{
    return mValues;
}

void Matrix::setValues(double **values)
{
    mValues = values;
}

void Matrix::outMatrix()
{
    cout << endl << "Матрица:" << endl;
    if (mColumns >= 20 && mRows >= 20)
    {
        cout << "Матрица слишком большая, чтобы выводить ее в консоль!" << endl;
    }
    else
    {
        for (size_t i = 0; i < mRows; i++)
        {
            for (size_t j = 0; j < mColumns; j++)
                cout << mValues[i][j] << "\t";
            cout << endl;
        }
    }
    cout << endl;
}

/**
 \throws InvalidMatrixSizeException
 */
Matrix* Matrix::operator+(const Matrix *matrix)
{
    Matrix* resultMatrix = new Matrix(mRows, mColumns);
    if (mRows != matrix->rows())
    {
        resultMatrix->setRows(0);
        resultMatrix->setColumns(0);
        throw new InvalidMatrixSizeException();
    }
    else
    {
        for (size_t i = 0; i < mRows; i++)
            for (size_t j = 0; j < mColumns; j++)
            {
                resultMatrix->mValues[i][j] = matrix->mValues[i][j] + mValues[i][j];
            }
    }
    return resultMatrix;
}

Matrix::Matrix(size_t rows, size_t columns, double **values)
    : mRows(rows), mColumns(columns)
{
    mValues = new double*[mRows];
    for (size_t i = 0; i < mRows; ++i)
    {
        mValues[i] = new double[mColumns];
        for (size_t j = 0; j < mColumns; j++)
            mValues[i][j] = values[i][j];
    }
}

Matrix::Matrix(size_t rows, size_t columns)
    : mRows(rows), mColumns(columns)
{
    mValues = new double*[mRows];
    for (size_t i = 0; i < mRows; ++i)
    {
        mValues[i] = new double[mColumns];
        for (size_t j = 0; j < mColumns; j++)
            mValues[i][j] = 0;
    }
}

Matrix::Matrix()
{

}


Matrix::~Matrix()
{
    for (size_t i = 0; i < mRows; ++i)
    {
        delete [] mValues[i];
        mValues[i] = nullptr;
    }
    delete [] mValues;
    mValues = nullptr;
}
