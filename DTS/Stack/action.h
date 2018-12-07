#ifndef ACTION_H
#define ACTION_H

#include <string>

class Action
{
public:
    typedef void (*action)();
private:
    std::string mMessage;
    action mOperation = nullptr;
public:
    Action(std::string message = "");
    Action(action operation ,std::string message = "");
    std::string message() const;
    void runAction();
};

#endif // ACTION_H
