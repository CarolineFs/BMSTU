#ifndef ROWTABLE_H
#define ROWTABLE_H

#include <iostream>
#include <vector>

//template <typename T>
class ColumnTable
{
    std::string mHeader;
    std::vector<std::string> mValues;
public:
    ColumnTable(std::string header) : mHeader(header) {}

    ~ColumnTable(){}

    void print(size_t idx)
    {
        std::cout << mValues[idx];
    }

    std::vector<std::string> values()
    {
        return mValues;
    }

    void addAllValues(std::vector<std::string> values)
    {
        mValues = values;
    }

    void addValue(std::string value)
    {
        mValues.push_back(value);
    }

    void insert(std::string value, size_t idx)
    {
        mValues.insert(mValues.begin() + idx, value);
    }

    void replace(std::string value, size_t idx)
    {
        mValues[idx] = value;
    }

    std::string remove(size_t idx)
    {
        std::string tmp = mValues[idx];
        mValues.erase(mValues.begin() + idx);
        return tmp;
    }
    std::string header() {return mHeader; }

    void setHeader(const std::string &header)
    {
        mHeader = header;
    }

};

#endif // ROWTABLE_H
