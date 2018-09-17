#include <stdio.h>
#include "arrayfilter.h"
#include "mysort.h"

#define EMPTY_FILTERED_ARRAY_CODE -2

int arrayFilterTest1(void);
int arrayFilterTest2(void);
int arrayFilterTest3(void);
int arrayFilterTest4(void);
int arrayFilterTest5(void);
int sortTest1(void);
int sortTest2(void);
int sortTest3(void);
int sortTest4(void);
int equalArrays(int* arrStart, int* arrEnd, int* arrStart2, int** arrEnd2);
int compareAscending(const void * x1, const void * x2);
int compareDescending(const void * x1, const void * x2);


void tests()
{
  int keyTestsPassed = 0;
  keyTestsPassed += arrayFilterTest1() + arrayFilterTest2() + arrayFilterTest3() +
                 arrayFilterTest4() + arrayFilterTest5();
  printf("Function key: \n%d tests from %d passed.\n", keyTestsPassed, 5);

  int mySortTestsPassed = 0;
  mySortTestsPassed += sortTest1() + sortTest2() + sortTest3() + sortTest4();

  printf("Function mySort: \n%d tests from %d passed.\n", mySortTestsPassed, 4);

}

int sortTest1()
{
  int code = 1;
  int array[7] = {1, 1, 4, 2, 1, 5, 9};
  int dstResArray[7] = {1, 1, 1, 2, 4, 5, 9};
  int* arrayEnd = array + 7;
  int* dstResArrEnd = dstResArray + 7;

  mySort(array, 7, sizeof (int), compareAscending);
  if (sizeof (array) / sizeof (array[0]) == sizeof (dstResArray) / sizeof (dstResArray[0])){
    code = equalArrays(array, arrayEnd, dstResArray, &dstResArrEnd); printf("\nIII");}
  else code = 0;

  printf("TEST1SORT %d", code);
  return code;
}

int sortTest2()
{
  int code = 1;
  int array[7] = {1, 1, 4, 2, 1, 5, 9};
  int dstResArray[7] = {9, 5, 4, 2, 1, 1, 1};
  int* arrayEnd = array + 7;
  int* dstResArrEnd = dstResArray + 7;

  mySort(array, 7, sizeof (int), compareDescending);
  if (sizeof (array) / sizeof (array[0]) == sizeof (dstResArray) / sizeof (dstResArray[0]))
    code = equalArrays(array, arrayEnd, dstResArray, &dstResArrEnd);
  else code = 0;

  return code;
}

int sortTest3()
{
  int code = 1;
  int array[3] = {1, 1, 1};
  int dstResArray[3] = {1, 1, 1, 1};
  int* arrayEnd = array + 3;
  int* dstResArrEnd = dstResArray + 3;

  mySort(array, 3, sizeof (int), compareAscending);
  if (sizeof (array) / sizeof (array[0]) == sizeof (dstResArray) / sizeof (dstResArray[0]))
    code = equalArrays(array, arrayEnd, dstResArray, &dstResArrEnd);
  else code = 0;

  return code;
}

int sortTest4()
{
  int code = 1;
  int array[7] = {1, -1, 4, 2, -1, 5, 9};
  int dstResArray[7] = {-1, -1, 1, 2, 4, 5, 9};
  int* arrayEnd = array + 7;
  int* dstResArrEnd = dstResArray + 7;

  mySort(array, 7, sizeof (int), compareAscending);
  if (sizeof (array) / sizeof (array[0]) == sizeof (dstResArray) / sizeof (dstResArray[0]))
    code = equalArrays(array, arrayEnd, dstResArray, &dstResArrEnd);
  else code = 0;

  return code;
}

int arrayFilterTest1()
{
  int code = 1;

  int array[10] = {2, 0, 1, 1, 4, 2, 1, 5, 9, 22};
  int dstResArray[7] = {1, 1, 4, 2, 1, 5, 9};

  int* dstResArrEnd = dstResArray + 7;
  int* arrayEnd = array + 10;

  int* resArr;
  int* resArrEnd;

  key(array, arrayEnd, &resArr, &resArrEnd);

  if (sizeof (array) / sizeof (array[0]) == sizeof (dstResArray) / sizeof (dstResArray[0]))
    code = equalArrays(resArr, resArrEnd, dstResArray, &dstResArrEnd);
  else code = 0;


  return code;
}

int arrayFilterTest2()
{
  int code = 1;

  int array[2] = {1, 2};
  int* arrayEnd = array + 2;

  int* resArr;
  int* resArrEnd;

  if (key(array, arrayEnd, &resArr, &resArrEnd) != EMPTY_FILTERED_ARRAY_CODE) code = 0;

  return code;
}

int arrayFilterTest3()
{
  int code = 1;

  int array[3] = {1, 1, 1};
  int* arrayEnd = array + 3;

  int* resArr;
  int* resArrEnd;

  if (key(array, arrayEnd, &resArr, &resArrEnd) != EMPTY_FILTERED_ARRAY_CODE) code = 0;

  return code;
}

int arrayFilterTest4()
{
  int code = 1;

  int array[5] = {34, 34, 4, 3, 0};
  int dstResArray[7] = {34, 4, 3};

  int* dstResArrEnd = dstResArray + 7;
  int* arrayEnd = array + 5;

  int* resArr;
  int* resArrEnd;

  key(array, arrayEnd, &resArr, &resArrEnd);

  if (sizeof (array) / sizeof (array[0]) == sizeof (dstResArray) / sizeof (dstResArray[0]))
    code = equalArrays(array, arrayEnd, dstResArray, &dstResArrEnd);
  else code = 0;

  return code;
}

int arrayFilterTest5()
{
  int code = 1;

  int array[8] = {5, 6, 0, 4, 0, 9, 4, 23};
  int dstResArray[4] = {4, 0, 9, 4};

  int* dstResArrEnd = dstResArray + 4;
  int* arrayEnd = array + 8;

  int* resArr;
  int* resArrEnd;

  key(array, arrayEnd, &resArr, &resArrEnd);

  if (sizeof (array) / sizeof (array[0]) == sizeof (dstResArray) / sizeof (dstResArray[0]))
    code = equalArrays(array, arrayEnd, dstResArray, &dstResArrEnd);
  else code = 0;

  return code;
}

int equalArrays(int* arrStart, int* arrEnd, int* arrStart2, int** arrEnd2)
{
  int* arrStartCopy = arrStart;
  int* arrStartCopy2 = arrStart2;
  int code = 1;
  while (arrStartCopy != arrEnd || arrStart2 != *arrEnd2)
  {
    if (*arrStartCopy != *arrStartCopy2)
    {
      code = 0;
      break;
    }
    arrStartCopy++;
    arrStartCopy2++;
  }
  return code;
}

int compareAscending(const void * x1, const void * x2)
{
  int val = *(const int*)x1 - *(const int*)x2;
  return val;
}

int compareDescending(const void * x1, const void * x2)
{
  int val = *(const int*)x2 - *(const int*)x1;
  return val;
}


