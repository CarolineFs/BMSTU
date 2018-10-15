#include <stdio.h>
#include <malloc.h>
#include "arrayfilter.h"
#include "mysort.h"
#include "compare.h"
#include "files.h"
#include <stdlib.h>
#include <string.h>
#include "tests.h"
#define OPEN_FILE_ERROR_MESSAGE "Unable to open file.\n"
#define EMPTY_ARRAY_CODE -1
#define EMPTY_FILTERED_ARRAY_CODE -2
#define CONST_CAST(x) (int*) x

int main(int argc, char** argv)
{
  printf("--------------------------------\n");
  printf("Testing program.\n");
  tests();
  printf("--------------------------------\n");
  FILE *f;
  char* IN_FILENAME;
  char* OUT_FILENAME;

  if (argc < 3)
  {
    //OUT_FILENAME = argv[2];
    printf("Too few arguments. Quitting...");
    exit(-1);
  }
  IN_FILENAME = argv[1];

  f = fopen(IN_FILENAME, "r");
  if (f != NULL)
  {
    printf("Reading the file...\n");

    unsigned int elements = 0;
    elements = countElementsInArray(f);

    printf("Read %d element in file...\n", elements);

//    if (elements <= 2)
//    {
//      printf("Too few elements in the array. Quitting...");
//      exit(EMPTY_ARRAY_CODE);
//    }

    int* array = (int*)malloc(elements*sizeof(int));
    if (array != NULL)
    {
      int* arrayEnd = array + elements;
      getArray(f, array, arrayEnd);

      int* filteredArray = array;
      int* filteredArrayEnd = arrayEnd;

      if (argc == 4 && strcmp(argv[3], "f") == 0)
      {
        key(array, arrayEnd, &filteredArray, &filteredArrayEnd);
        //int filter_flag = key(array, arrayEnd, &filteredArray, &filteredArrayEnd);
        printf("Array filtered...\n");
//        if (filter_flag == -2)
//        {
//          printf("Filtered array is empty. Quitting...");
//          exit(EMPTY_FILTERED_ARRAY_CODE);
//        }
      }
      size_t number =  (size_t)(filteredArrayEnd - filteredArray);

      mySort(filteredArray, number, sizeof(*filteredArray), compare);
      printf("Array sorted...\n");

      OUT_FILENAME = argv[2];
      writeFile(&filteredArray, &filteredArrayEnd, OUT_FILENAME);

      free(array);
    }
    else
      printf("Unable to allocate memory.\n");
  }
  else
  {
    printf(OPEN_FILE_ERROR_MESSAGE);
    puts(IN_FILENAME);
  }
  fclose(f);

  return 0;
}
