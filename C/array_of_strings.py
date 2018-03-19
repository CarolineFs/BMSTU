/*
 * Функция, позволяющая вносить новую строку с клавиатуры в массив (массив на 10 строк)
 * Функция, позволяющая редактировать одну из записей в массиве по номеру (вводятся номер и новая строка)
 * Функция, определяющая, сколько строк в массиве соответствуют введенной пользователем
*/

#include <stdio.h>
#include <string.h>
#define ARRAY_LEN 10
#define MAX_STR_LEN 255


void* get_array(char* two_dim_array)
{
    
}


int main()
{
    char* two_dim_array[ARRAY_LEN][MAX_STR_LEN];


   //get_array(two_dim_array);

   for (unsigned int i = 0; i < ARRAY_LEN; ++i)
   {
       printf("Input string %u: ", i+1);
       fgets(two_dim_array[i], MAX_STR_LEN, stdin);
       fputs(two_dim_array[i], stdout);
   }


   return 0;
}

/*
#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char* buf = NULL;
    size_t len;

    puts("Input a line:");
    if(getline(&buf, &len, stdin) == -1 && ferror(stdin))
    err(1, "getline");

    printf("You've entered %u character(s) (including newline):\n%s", strlen(buf), buf);

    free(buf);

    exit(0);
}*/
