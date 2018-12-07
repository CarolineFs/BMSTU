#ifndef MENU_H
#define MENU_H

#include "action.h"
#include <vector>

class Menu
{
    std::vector<Action> mActions;
    std::vector<std::string> mTitles;
public:
    enum StackType { DYMAMIC, STATIC };
    Menu();
    void addAction(Action action);
    void addTitle(std::string title);
    void create();
    void inputAction();
};

#endif // MENU_H
