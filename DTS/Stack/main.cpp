#include <iostream>
#include <string>
#include "staticstack.h"
#include "dynamicstack.h"
#include "staticqueue.h"
#include "dynamicqueue.h"
#include "menu.h"
#include "filehelper.h"
#include "ColumnTable.h"
#include <ctime>
#include <time.h>
#include "table.h"

void submenuStaticStack();
void submenuDynamicStack();
void finish();
void pushStatic();
void pushDynamic();
void printStatic();
static void printDynamic();
void popStatic();
void popDynamic();
void cleanStatic();
void cleanDynamic();
static void printAndCleanDynamic();
std::string getString();
void createUpperMenu();
void printAndCleanStatic();
double tickStaticTime(StaticStack<std::string>* stack);
double tickDynamicTime(DynamicStack<std::string> *stack);
void measure();
unsigned long long tick(void);


static StaticStack<std::string> staticStack(4);
static DynamicStack<std::string> dynamicStack;

int main()
{
    createUpperMenu();
//    menu.addAction(Action(helloWorld,"Print"));
//    menu.addAction(Action(justHello,"Pop"));
//    menu.addAction(Action(exit,"Push"));
//    menu.create();
//    menu.inputAction();

//  StaticStack <std::string> s(5);
////  s.pop();
//  s.push("s1");
//  s.print();
//  s.push("s2");
//  s.print();
//  s.push("s3");
//  s.print();
//  s.push("s4");
//  s.print();
//  s.push("s5");
//  s.print();
//  std::string i = s.pop();
//  s.push("s6");
//  s.print();
//  try {
//    s.push("exception");
//  } catch (...) {
//      exit(EXIT_FAILURE);
//  }
//  _____________________________________________________
//  DynamicStack <std::string> d;
//  d.push("first string");
//  d.print(DynamicStack<std::string>::ADDRESS);
//  d.pop();
//  d.push("3");
//  d.push("second ");
//  d.print(DynamicStack<std::string>::ADDRESS, DynamicStack<std::string>::POP);
//  d.push("12");
//  d.pop();
//  d.print(DynamicStack<std::string>::ADDRESS);
//  _____________________________________________________
//  StaticQueue <std::string> sq(5);
//  sq.push("s1");
//  sq.print();
//  sq.push("s2");
//  sq.pop();
//  sq.print();
//  sq.push("s3");
//  sq.push("s4");
//  sq.push("s5");
//  sq.push("s6");
//  try {
//    sq.push("s7");
//  } catch (...) {
//    sq.print();
//  }
//  sq.pop();
//  sq.pop();
//  sq.print();
//  ____std::vector<long> staticT;
//  StaticStack<int> s(10);
//  DynamicQueue <int> dq;
//  dq.push(5);
//  dq.print();
//  dq.push(10);
//  int i = dq.pop();
//  dq.push(15);
//  dq.push(20);
//  dq.print();
//  dq.push(25);
//  int j = dq.pop();
//  dq.print();
  return 0;
}


void measure()
{
    std::string path = "/home/syzygy/Desktop/git/c/Stack/Database/";
    StaticStack<std::string> static10 = FileHelper::getStaticStack(path + "stack10");
    DynamicStack<std::string> dynamic10 = FileHelper::getDynamicStack(path + "stack10");

    StaticStack<std::string> static50 = FileHelper::getStaticStack(path + "stack50");
    DynamicStack<std::string> dynamic50 = FileHelper::getDynamicStack(path + "stack50");

    StaticStack<std::string> static100 = FileHelper::getStaticStack(path + "stack100");
    DynamicStack<std::string> dynamic100 = FileHelper::getDynamicStack(path + "stack100");

    StaticStack<std::string> static200 = FileHelper::getStaticStack(path + "stack200");
    DynamicStack<std::string> dynamic200 = FileHelper::getDynamicStack(path + "stack200");

    StaticStack<std::string> static1000 = FileHelper::getStaticStack(path + "stack1000");
    DynamicStack<std::string> dynamic1000 = FileHelper::getDynamicStack(path + "stack1000");

    StaticStack<std::string>* staticStacksContainer[] =    { &static10,
                                                             &static50,
                                                             &static100,
                                                             &static200,
                                                             &static1000 };
    DynamicStack<std::string>* dynamicStacksContainer[] =  { &dynamic10,
                                                             &dynamic50,
                                                             &dynamic100,
                                                             &dynamic200,
                                                             &dynamic1000 };

    ColumnTable  column1("Size");
    ColumnTable column2("Static : time");
    ColumnTable column3("Dynamic : time");
    ColumnTable column4("Static : memory");
    ColumnTable column5("Dynamic : memory");


    for (size_t i = 0; i < 5; ++i)
    {
        column4.addValue(std::to_string(staticStacksContainer[i]->getBytesSize()));
        column5.addValue(std::to_string(dynamicStacksContainer[i]->getBytesSize()));
        column2.addValue(std::to_string(tickStaticTime(staticStacksContainer[i])));
        column3.addValue(std::to_string(tickDynamicTime(dynamicStacksContainer[i])));
    }

    column1.addAllValues(std::vector<std::string>() = {"10", "50", "100", "200", "1000"});

    Table table(5, 5);
    table.setColumnsContent(std::vector<ColumnTable>() = {column1, column2, column3, column4, column5});
    table.print();
}

double tickStaticTime(StaticStack<std::string>* stack)
{
    uint64_t  start = 0,
              end   = 0;
    start = tick();
    stack->print();
    end = tick();
    double res = (end - start)/2.5;
    return  res;
}

double tickDynamicTime(DynamicStack<std::string>* stack)
{
    uint64_t  start = 0,
              end   = 0;
    start = tick();
    stack->print();
//    stack->printParam(DynamicStack<std::string>::Mode::ADDRESS, DynamicStack<std::string>::Dropped::POP);
    end = tick();
    double res = (end - start)/2.5;
    return res;
}

unsigned long long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d) );
    return d;
}

void createUpperMenu()
{
    Menu upperMenu;
    upperMenu.addTitle("Программа распечатывает слова в обратном порядке");
    upperMenu.addTitle("Выберите тип стека");
    upperMenu.addAction(Action(submenuStaticStack, "статический"));
    upperMenu.addAction(Action(submenuDynamicStack, "динамический стек"));
    upperMenu.addAction(Action(measure, "провести оценку эффективности"));
    upperMenu.addAction(Action(finish, "выход"));
    upperMenu.create();
    upperMenu.inputAction();
}

std::string getString()
{
    std::string str;

    std::cout << "Введите строку: " << std::endl;
    std::cin >> str;

    return str;
}

void pushStatic()
{
    std::string string = getString();
    try {
        staticStack.push(string);
    } catch (...) {
        std::cout << "Переполнение стека" << std::endl;
    }
    submenuStaticStack();
}

void pushDynamic()
{
    std::string string = getString();
    dynamicStack.push(string);
    submenuDynamicStack();
}

void popDynamic()
{
    try {
        dynamicStack.pop();
    } catch (...) {
        std::cout << "Стек пустой" << std::endl;
    }
    submenuDynamicStack();
}

void popStatic()
{
    try {
        staticStack.pop();
    } catch (...) {
        std::cout << "Стек пустой" << std::endl;
    }
    submenuStaticStack();
}

void cleanStatic()
{
    staticStack.clean();
    submenuStaticStack();
}

void cleanDynamic()
{
    dynamicStack.clean();
    submenuDynamicStack();
}

void printStatic()
{
    staticStack.printNoDelete();
    submenuStaticStack();
}

void printAndCleanStatic()
{
    staticStack.print();
    submenuStaticStack();
}

void finish ()
{
    exit(0);
}

static void printDynamic()
{
    dynamicStack.printParam(DynamicStack<std::string>::Mode::ADDRESS, DynamicStack<std::string>::Dropped::NONE);
    submenuDynamicStack();
}

static void printAndCleanDynamic()
{
    dynamicStack.printParam(DynamicStack<std::string>::Mode::ADDRESS, DynamicStack<std::string>::Dropped::POP);
    submenuDynamicStack();
}

void submenuStaticStack()
{
    Menu staticSubMenu;
    staticSubMenu.addTitle("Выберите действие");
    staticSubMenu.addAction(Action(popStatic, "удалить элемент"));
    staticSubMenu.addAction(Action(pushStatic, "добавить элемент"));
    staticSubMenu.addAction(Action(printAndCleanStatic, "просмотр состояния стека (c удалением элементов)"));
    staticSubMenu.addAction(Action(printStatic, "просмотр состояния стека (без удаления элементов)"));
    staticSubMenu.addAction(Action(cleanStatic, "очистить стек"));
    staticSubMenu.addAction(Action(createUpperMenu , "назад"));
    staticSubMenu.create();
    staticSubMenu.inputAction();
}

void submenuDynamicStack()
{
    Menu submenu;
    submenu.addTitle("Выберите действие");
    submenu.addAction(Action(printAndCleanDynamic, "просмотр состояния стека (c удалением элементов)"));
    submenu.addAction(Action(printDynamic, "просмотр состояния стека (без удаления элементов)"));
    submenu.addAction(Action(popDynamic, "удалить элемент"));
    submenu.addAction(Action(pushDynamic, "добавить элемент"));
    submenu.addAction(Action(cleanDynamic, "очистить стек"));
    submenu.addAction(Action(createUpperMenu , "назад"));
    submenu.create();
    submenu.inputAction();
}

