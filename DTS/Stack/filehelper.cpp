#include "filehelper.h"
#include <fstream>

FileHelper::FileHelper()
{

}

DynamicStack<std::string> FileHelper::getDynamicStack(std::string filename)
{
    std::string buff;
    std::vector<std::string> strings;

    std::fstream file(filename);
    while (!file.eof()) {
        getline(file, buff);
        if (buff.empty()) break;
        std::vector<std::string> splitString = split(buff, ' ');
        for (std::vector<std::string>::iterator iter = splitString.begin(); iter != splitString.end(); ++iter)
        {
            strings.push_back(*iter);
        }
    }
    DynamicStack<std::string> dynamicStack;
    for (std::vector<std::string>::iterator iter = strings.begin(); iter != strings.end(); iter++)
    {
        dynamicStack.push(*iter);
    }
    file.close();
    return dynamicStack;
}

StaticStack<std::string> FileHelper::getStaticStack(std::string filename)
{
    std::string buff;
    std::vector<std::string> strings;

    std::fstream file(filename);
    if (!file.is_open())
        std::cout << "FILE NOT OPEN" << std::endl;
    while (!file.eof()) {
        getline(file, buff);
        if (buff.empty()) break;
        std::vector<std::string> splitString = split(buff, ' ');
        for (std::vector<std::string>::iterator iter = splitString.begin(); iter != splitString.end(); ++iter)
        {
            strings.push_back(*iter);
        }
    }
    StaticStack<std::string> staticStack(strings.size());
    for (std::vector<std::string>::iterator iter = strings.begin(); iter != strings.end(); iter++)
    {
        staticStack.push(*iter);
    }
    file.close();

    return staticStack;
}

std::vector<std::string> FileHelper::split(std::string text, char splitter)
{
  std::string buffer;
  std::vector<std::string> strings;
  for (const char c : text)
  {
      if (c != splitter) buffer.push_back(c);
      else
      {
          strings.push_back(buffer);
          buffer.clear();
      }
    }
  if(!buffer.empty()) strings.push_back(buffer);
  return strings;
}
