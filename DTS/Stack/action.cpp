#include "action.h"

Action::Action(std::string message)
    : mMessage(message)
{

}

Action::Action(Action::action operation, std::string message)
    : mMessage(message), mOperation(operation)
{

}

std::string Action::message() const
{
    return mMessage;
}

void Action::runAction()
{
//    if (mOperation != nullptr)
        mOperation();
//    else
//        throw std::bad_exception();
}
