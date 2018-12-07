#ifndef MYEXCEPTIONS_H
#define MYEXCEPTIONS_H

#include <iostream>

class InvalidMatrixSizeException : public std::exception {};

class OpenFileException : public std::exception{};

class InvalidDataException  : public std::exception{};

#endif // MYEXCEPTIONS_H
