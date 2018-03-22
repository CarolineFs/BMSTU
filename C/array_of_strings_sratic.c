/*
 * Функция, позволяющая вносить новую строку с клавиатуры в массив (массив на 10 строк)
 * Функция, позволяющая редактировать одну из записей в массиве по номеру (вводятся номер и новая строка)
 * Функция, определяющая, сколько строк в массиве соответствуют введенной пользователем
 */

#include <stdio.h>
#include <string.h>
#define ARRAY_LEN 3
#define MAX_STRING_LEN 255

int input_error_preventer();

int main()
{
    char** two_dim_array[ARRAY_LEN][MAX_STRING_LEN];
    // Input array
    for (unsigned int i = 0; i < ARRAY_LEN; ++i)
    {
        printf("Input %u string: ", i);
        fgets(two_dim_array[i], MAX_STRING_LEN, stdin);
    }

    //get_array(two_dim_array);


    // String redactor
    printf("\nInput index of the string you want to change: ");
    int idx = input_error_preventer();

    while ((idx >= ARRAY_LEN) || (idx < 0))
    {
        printf("Input error. No such string number: ");
        idx = input_error_preventer();
    }

    printf("Input new %d string: ", idx);
    fgets(two_dim_array[idx], MAX_STRING_LEN, stdin);


    // Strings comparrison
    char* compare_string[MAX_STRING_LEN];
    unsigned int flag = 0;
    printf("\nInput the string you want to compare: ");
    fgets(compare_string, MAX_STRING_LEN, stdin);
    for (unsigned int i = 0; i < ARRAY_LEN; ++i)
    {
        if (strcmp(two_dim_array[i], compare_string) == 0)
        {
            printf("Your string coincides with the %u string in the array.\n", i);
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        printf("There are no such strings in the array. ");

    return 0;
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


void get_array(char** two_dim_array)
{
    for (unsigned int i = 0; i < ARRAY_LEN; ++i)
    {
        printf("Input %u string: ", i + 1);
        fgets(two_dim_array[i], MAX_STRING_LEN, stdin);
    }
}
