TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        main.cpp \
    matrix.cpp \
    sparsematrix.cpp \
    firstincolumn.cpp \
    myexceptions.cpp \
    functor.cpp

HEADERS += \
    matrix.h \
    sparsematrix.h \
    firstincolumn.h \
    myexceptions.h \
    functor.h
