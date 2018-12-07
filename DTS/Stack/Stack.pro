TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        main.cpp \
    menu.cpp \
    action.cpp \
    filehelper.cpp

HEADERS += \
    dynamicstack.h \
    staticstack.h \
    absractcontainer.h \
    staticqueue.h \
    dynamicqueue.h \
    menu.h \
    action.h \
    filehelper.h \
    table.h \
    ColumnTable.h \
    interface.h
