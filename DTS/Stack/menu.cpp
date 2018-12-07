#include "menu.h"
#include <iostream>

Menu::Menu()
{

}

void Menu::addAction(Action a)
{
    mActions.push_back(a);
}

void Menu::addTitle(std::string title)
{
    mTitles.push_back(title);
}

void Menu::create()
{
//   Вывести на экран
    for (std::vector<std::string>::iterator iter = mTitles.begin(); iter != mTitles.end(); ++iter)
    {
        std::cout << *iter << std::endl;
    }
    uint32_t counter = 0;
    for (Action a : mActions) {
        std::cout << ++counter << ") - " << a.message() << std::endl;
    }
}

void Menu::inputAction()
{
    uint32_t answer = 0;
    std::cin >> answer;
    if (answer <= mActions.size())
    {
        std::cout << "Вы выбрали:" << ' ' << mActions[answer - 1].message() << std::endl;
        mActions[answer - 1].runAction();
    }
    else
        std::cout << "Вы выбрали:" << "---" << std::endl;
}
