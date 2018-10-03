#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#define FILENAME "C:\\Users\\novoc\\Desktop\\in_1.txt"
#define FILENAME2 "C:\\Users\\n3ovoc\\Desktop\\in_2.txt"
#define FILENEME_OUT "C:\\Users\\novoc\\Desktop\\in_1.txt"
#define OPEN_FILE_ERROR_MESSAGE "Unable to open file.\n"

int* readFile(char*);
int** allocMatrix(size_t, size_t);
void freeMatrix(int**, size_t);
void writeFile(char*, int**, size_t, size_t);
int* addMatrixes(int**, size_t, size_t, int** , size_t, size_t);
int* multiplyMatrixes(int**, size_t, size_t, int**, size_t, size_t);

int main()
{
  readFile(FILENAME);
  return 0;
}

int* multiplyMatrixes(int**matrix1, size_t rows1, size_t columns1, int** matrix2, size_t rows2, size_t columns2)
{

}

int* addMatrixes(int** matrix1, size_t rows1, size_t columns1, int** matrix2, size_t rows2, size_t columns2)
{
  if (rows1 != rows2 && columns1 != columns2)
    return NULL;
  int* resultMatrix;
  resultMatrix = *allocMatrix(rows1, columns1);
  for (size_t i = 0; i < rows1; i++)
  {
    int* place1 = matrix1[i];
    int* place2 = matrix2[i];
    int* resPlace = &resultMatrix[i];
    for (size_t j = 0; j < columns1; j++)
    {
      *resPlace = *place1 + *place2;
      place1++;
      place2++;
      resPlace++;
    }
  }
  return resultMatrix;
}

void writeFile(char* filename, int** matrix, size_t rows, size_t columns)
{
  FILE* f;
  f = fopen(filename, "w");
  if (f != NULL)
  {
    fprintf(f, "%d %d", rows, columns);
    for (size_t i = 0; i < rows; i++)
    {
      int* place = matrix[i];
      for (size_t j = 0; j < columns; j++)
      {
        fprintf(f, "%d", *place);
        place++;
        if (j == columns) fprintf(f, "\n");
      }
    }
  }
  else
  {
    printf(OPEN_FILE_ERROR_MESSAGE);
    puts(filename);
  }
  fclose(f);
}

int* readFile(char* filename)
{
  int* matrix;

  FILE* f;
  f = fopen(filename, "r");
  if (f != NULL)
  {
    size_t rows;
    size_t columns;
    if (!feof(f))
    {
      if (fscanf(f, "%d %d", &columns, &rows) != 2)
      {
        printf("Incorrect data in the file.\n");
        exit(-1);
      }
    }
    matrix = *allocMatrix(rows, columns);
    for (size_t i = 0; i < rows; i++)
    {
      int* place = &matrix[i];
      for (size_t j = 0; j < columns; j++)
      {
        fscanf(f, "%d", place);
        place++;
      }
    }
  }
  else
  {
    printf(OPEN_FILE_ERROR_MESSAGE);
    puts(filename);
    matrix = NULL;
  }
  fclose(f);

  return matrix;
}

int** allocMatrix(size_t n, size_t m)
{
  int** data = calloc(n, sizeof (int*));
  if (!data) return NULL;
  for (size_t i = 0; i < n; i++)
  {
    data[i] = malloc(m * sizeof (int));
    if (!data[i])
    {
      freeMatrix(data, n);
      return NULL;
    }
  }
  return data;
}

void freeMatrix(int** a, size_t n)
{
  for (size_t i = 0; i < n; i++)
    free(a[i]);
  free(a);
}
