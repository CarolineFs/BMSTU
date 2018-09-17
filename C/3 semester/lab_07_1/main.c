#include <stdio.h>
#include <malloc.h>
#include "arrayfilter.h"
#include "mysort.h"
#include <stdlib.h>
#include "tests.h"
#include <string.h>
#ifdef _WIN32|_WIN64
#define FILENAME "C:\\Users\\novoc\\Desktop\\lab_07_1.txt"
  #define OUT_FILENAME "C:\\Users\\novoc\\Desktop\\lab_07_1_out.txt"
#else
  #define FILENAME "/home/oem/Desktop/lab_07_1"
  #define OUT_FILENAME ""
#endif
#define OPEN_FILE_ERROR_MESSAGE "Unable to open file.\n"
#define EMPTY_ARRAY_CODE -1
#define EMPTY_FILTERED_ARRAY_CODE -2
#define CONST_CAST(x) (int*) x


unsigned int countElementsInArray(FILE* f);
void getArray(FILE* f, int* startPtr, int* endPtr);
int compare(const void*, const void*);
void writeFile(int**, int**);

int main(int argc, char** argv)
{
  tests();
//  FILE *f;

//  f = fopen(FILENAME, "r");
//  if (f != NULL)
//  {
//    printf("Reading the file...\n");

//    unsigned int elements = 0;
//    elements = countElementsInArray(f);

//    printf("Read %d element in file...\n", elements);

//    if (elements <= 2)
//    {
//      printf("Too few elements in the array. Quitting...");
//      exit(EMPTY_ARRAY_CODE);
//    }

//    int* array = (int*)malloc(elements*sizeof(int));
//    int* arrayEnd = array + elements;
//    getArray(f, array, arrayEnd);

//    int* filteredArray = array;
//    int* filteredArrayEnd = arrayEnd;

//    if (argc == 4 && strcmp(argv[3], "f") == 0)
//    {
//      int filter_flag = key(array, arrayEnd, &filteredArray, &filteredArrayEnd);
//      printf("Array filtered...\n");
//      if (filter_flag == -2)
//      {
//        printf("Filtered array is empty. Quitting...");
//        exit(EMPTY_FILTERED_ARRAY_CODE);
//      }
//    }

//    size_t number =  (size_t)(filteredArrayEnd - filteredArray);

//    mySort(filteredArray, number, sizeof(*filteredArray), compare);
//    printf("Array sorted...\n");

//    writeFile(&filteredArray, &filteredArrayEnd);

//    free(array);
//  }
//  else
//  {
//    printf(OPEN_FILE_ERROR_MESSAGE);
//  }
//  fclose(f);


  return 0;
}


void writeFile(int ** start, int ** end)
{
  FILE *f;
  f = fopen(OUT_FILENAME, "w");
  if (f != NULL)
  {
    while (*start != *end)
    {
      fprintf(f, "%d ", **start);
      (*start)++;
    }

  }
  else
  {
    printf("ResultL ");
    printf(OPEN_FILE_ERROR_MESSAGE);
  }
  fclose(f);
}


int compare(const void * x1, const void * x2)
{
  int val = *(const int*)x1 - *(const int*)x2;
  return val;
}

void getArray(FILE* f, int* startPtr, int* endPtr)
{
  int* startPtrCopy = startPtr;
  while (startPtrCopy != endPtr)
  {
    fscanf(f, "%d", startPtrCopy);
    startPtrCopy++;
  }

}

unsigned int countElementsInArray(FILE* f)
{
  unsigned int elementsCount = 0;

  while(1)
  {
    if (feof(f)) break;
    int buffInt;
    if (fscanf(f, "%d", &buffInt) != 1) break;
    elementsCount++;
  }
  fseek(f, 0, SEEK_SET);
  return elementsCount;
}
