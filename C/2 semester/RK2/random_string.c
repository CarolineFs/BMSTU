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
unsigned int size;
char separator;
char **matrix;

void matrix_generator();
void cut_string();

int main()
{
  srand(time(NULL));
  printf("Input a separator: ");
  scanf("%c", &separator);
  printf("Input size of matrix: ");
  scanf("%d", &size);

  matrix_generator();

  free(matrix);
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

    printf("%s\n", matrix[i]);


  }
  cut_string();

  printf("\n\n");
  for (size_t i = 0; i < size; ++i)
    printf("%s\n", matrix[i]);
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
    printf("%u %u\n", k_upper, k_lower);

    if (k_lower < k_upper)
    {
      cut(i);
      --i;
      --size;
      continue;
    }
  }
}
