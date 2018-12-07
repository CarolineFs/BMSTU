#ifndef FILEHELPER_H
#define FILEHELPER_H

#include "staticstack.h"
#include "dynamicstack.h"

class FileHelper
{
public:
    FileHelper();
    static DynamicStack<std::string> getDynamicStack(std::string filename);
    static StaticStack<std::string> getStaticStack(std::string filename);
    static std::vector<std::string> split(std::string text, char splitter);
};

#endif // FILEHELPER_H
