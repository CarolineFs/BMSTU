#ifndef TABLE_H
#define TABLE_H

#include <iostream>
#include <stdint.h>
#include <vector>
#include "ColumnTable.h"

class Table
{
    const uint16_t mColumnSize = 30;
    uint32_t mColumns;
    uint32_t mRows;
    std::vector<ColumnTable> mColumnsContent;
    std::string multiplyString(std::string string, unsigned long size)
    {
        std::string strCopy = string;
        while (string.size() <= size) {
            string.append(strCopy);
        }
        return string;
    }
public:
    Table(uint32_t columns, uint32_t rows) : mColumns(columns), mRows(rows) {}

    uint32_t columns() const;
    void setColumns(const uint32_t &columns);
    std::vector<std::string> headlines() const;
    void setHeadlines(const std::vector<std::string> &headlines);
    uint32_t rows() const;
    void setRows(const uint32_t &rows);
    std::vector<std::vector<std::string> > columnsContent() const;
    void setColumnsContent(std::vector<ColumnTable> columnsContent)
    {
        mColumnsContent = columnsContent;
    }

    void print()
    {
        uint32_t sizeString = 110; // +
        std::cout << multiplyString("-", sizeString + 9/*mColumnSize * 3 + 6*/) << std::endl;
        uint32_t sizeColString = sizeString / mColumnsContent.size(); // +
        for (size_t i = 0; i < mColumnsContent.size(); ++i)
        {
            std::string head = mColumnsContent[i].header();
            uint32_t sizeHeader = sizeColString - mColumnsContent[i].header().size(); // +
            uint32_t sizeOffset = sizeHeader / 2; // +

            std::cout << /*"|    "*/'|' << multiplyString(" ",sizeOffset - 1)
                      << mColumnsContent[i].header()
                      << multiplyString(" ", sizeOffset - 1)
                      << ((sizeHeader % 2 == 0) ? "" : " ")
                      << '|'
                         /*multiplyString(" ", mColumnSize + 4 - mColumnsContent[i].header().size())*/; // +
        }
        std::cout << std::endl << multiplyString("-", sizeString + 9/*mColumnSize * 3 + 6*/) << std::endl;
        for (size_t j = 0; j < mRows; ++j)
        {
            for (size_t i = 0; i < mColumns; ++i)
            {
                std::string current = mColumnsContent[i].values().at(j);
                uint32_t sizeHeader = sizeColString - current.size();
                uint32_t sizeOffset = sizeHeader / 2;
                std::cout << /*"|    "*/ '|' << multiplyString(" ", sizeOffset - 1)
                          << current
                          << multiplyString(" ", sizeOffset - 1)
                          << ((sizeHeader % 2 == 0) ? "" : " ")
                          << '|';
            }
            std::cout <<  "|" << std::endl;
        }
        std::cout << multiplyString("-", /*mColumnSize * 3 + 6*/sizeString + 9) << std::endl;
    }

};

#endif // TABLE_H
