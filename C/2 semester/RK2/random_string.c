/* 1. Двумерный массив из букв нижнего в верхнего регистра и одгого раделителя для каждой строки
 * (разделитель вводится с клавиатуры)
 * для каждой строки в случае, если количество букв нижнего регистра до разделителя меньше
 * количества букв верхнего регистра, сократить саму строку.
 * Вывести получившийся массив.
 * Разделитель и размер квадратной матрицы вводятся пользователем.
 *
 * 2. Для адресной книги (записи в текстовом файле формата Фамилия Адрес Телефон (8499 *** ** **))
 * Реализовать вывод данных на экран, добавление нового элемента, сохранение файла.
 */

#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>
#define UPPER_LETTERS "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
#define LOWER_LETTERS "abcdefghigklmnopqrstuvwxcyz"
void matrix_generator();
void cut_string();
int input_error_preventer();
void print_matrix(size_t size, size_t len);

unsigned int size;
char separator;
char **matrix;


int main()
{
  srand(time(NULL));
  printf("Input a separator: ");
  scanf("%c", &separator);
  printf("Input size of matrix: ");
  size = input_error_preventer();

  unsigned int len = size;

  matrix_generator();
  print_matrix(size, len);

  printf("Cut matrix:\n");
  cut_string();
  print_matrix(size, len);

  free(matrix);
}


void print_matrix(size_t size, size_t len)
{
  printf("\n");
  for (size_t i = 0; i < size; ++i)
  {
    for (size_t j = 0; j < len; ++j)
      printf("%c", matrix[i][j]);
    printf("\n");
  }
  printf("\n");
}


void matrix_generator()
{
  matrix = (char**)malloc((size)*sizeof(char*)); // Выделение памяти под указатели на строки

  for (size_t i = 0; i < size; ++i)
  {
    matrix[i] = (char*)malloc((size-1)*sizeof(char));
    size_t sep_idx = 0 + rand() % (size-1);

    for (size_t j = 0; j < size; ++j)
    {
      size_t idx = 0 + rand() % 26;
      size_t chose_register = 0 + rand() % 2;

      if (j != sep_idx)
      {
        if (chose_register == 0)
          matrix[i][j] = UPPER_LETTERS[idx];
        else
          matrix[i][j] = LOWER_LETTERS[idx];
      }
      else
        matrix[i][j] = separator;
    }
  }
}


_Bool is_upper(char letter)
{
  for (size_t i = 0; i < 26; ++i)
    if (letter == UPPER_LETTERS[i])
      return 1;
  return 0;
}


void cut(size_t idx)
{
  for (size_t i = 0; i < size; ++i)
    if (i > idx)
      strcpy(matrix[i-1], matrix[i]);
}


void cut_string()
{
  for (size_t i = 0; i < size; ++i)
  {
    _Bool before_sep = 1;
    size_t k_upper = 0;
    size_t k_lower = 0;
    for (size_t j = 0; j < size; ++j)
    {
      k_upper += is_upper(matrix[i][j]);
      if (matrix[i][j] == separator)
        before_sep = 0;
      k_lower += before_sep*!is_upper(matrix[i][j]);
    }

    if (k_lower < k_upper)
    {
      cut(i);
      --i;
      --size;
      continue;
    }
  }
}


int input_error_preventer()
{
    int x, rc;
    char tmp;

    while (((rc = scanf("%d%c", &x, &tmp)) != 2 && rc != EOF) || tmp != '\n')
    {
        printf("Input error. Please, enter an integer: ");
        do
        {
        rc = scanf("%c", &tmp);
        }
        while(rc != EOF && tmp != '\n');
    }
    return x;
}
