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
#define UPPER_LETTERS "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
#define LOWER_LETTERS "abcdefghigklmnopqrstuvwxcyz"
unsigned int size;
char separator;
char **matrix;


int main()
{
  srand(time(NULL));
  printf("Input a separator: ");
  scanf("%c", &separator);
  printf("Input size of matrix: ");
  scanf("%d", &size);
  matrix = (char**)malloc((size)*sizeof(char*)); // Выделение памяти под указатели на строки

  for (size_t i = 0; i < size; ++i)
  {
    matrix[i] = (char*)malloc((size-1)*sizeof(char));
    for (size_t j = 0; j < size; ++j)
    {
      int idx = 0 + rand() % 25;
      if (j != size-1)
        matrix[i][j] = UPPER_LETTERS[idx];
      else
        matrix[i][j] = separator;

    }
    printf("%s\n", matrix[i]);

  }

  free(matrix);


}
