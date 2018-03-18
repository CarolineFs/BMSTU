/*
 * Функция, позволяющая вносить новую строку с клавиатуры в массив (массив на 10 строк)
 * Функция, позволяющая редактировать одну из записей в массиве по номеру (вводятся номер и новая строка)
 * Функция, определяющая, сколько строк в массиве соответствуют введенной пользователем
 */

#include <stdio.h>
#include <string.h>
#define LEN 10
#define MAX_STR_LEN 255

int main()
{
    char* str;
    char* two_dim_array[LEN][MAX_STR_LEN];
    for (size_t i; i < LEN; i++)
    {
        printf("Input new string: ");
        fgets(two_dim_array[i], 10);

    }
}
