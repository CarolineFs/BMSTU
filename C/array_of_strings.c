/*
 * Функция, позволяющая вносить новую строку с клавиатуры в массив (массив на 10 строк)
 * Функция, позволяющая редактировать одну из записей в массиве по номеру (вводятся номер и новая строка)
 * Функция, определяющая, сколько строк в массиве соответствуют введенной пользователем
 */


#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY_LEN 4


void compare_strings(char* two_dim_array)
{
    char* comp_string = NULL;
    size_t len;

    puts("Input a string you want to compare with strings in the array: ");
    if(getline(&comp_string, &len, stdin) == -1 && ferror(stdin))
        err(1, "getline");

    for (unsigned int i = 0; i < ARRAY_LEN; ++i)
        if (strcmp(&two_dim_array[i], comp_string) == 0)
        {
            printf("Your string coincides with the %u string in the array.\n", i);
            break;
        }


}


int main(void)
{
    char* two_dim_array [ARRAY_LEN] = {NULL};
    size_t len;

    for (unsigned int i = 0; i < ARRAY_LEN; ++i)
    {
        puts("Input a line:");
        if(getline(&two_dim_array[i], &len, stdin) == -1 && ferror(stdin))
            err(1, "getline");
    }


    /*unsigned int change_idx;
    size_t l;

    printf("Input the number of string you want to edit: ");
    scanf("%u", &change_idx);
    //fflush(stdin);
    const size_t idx = change_idx;
    puts("Input a line: ");
    //fflush(stdin);
    if(getline(&two_dim_array[idx], &l, stdin) == -1 && ferror(stdin))
        err(1, "getline");*/

    //compare_strings(two_dim_array);

    char* comp_string = NULL;

    puts("\nInput a string you want to compare with strings in the array: ");
    if(getline(&comp_string, &len, stdin) == -1 && ferror(stdin))
        err(1, "getline");

    for (unsigned int i = 0; i < ARRAY_LEN; ++i)
        if (strcmp(two_dim_array[i], comp_string) == 0)
        {
            printf("Your string coincides with the %u string in the array.\n", i);
            break;
        }

    for (size_t i = 0; i < ARRAY_LEN; ++i)
        free(two_dim_array[i]);

    exit(0);
}
