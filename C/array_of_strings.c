#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY_LEN 5

int main(void)
{
    char* two_dim_array [ARRAY_LEN] = {NULL};
    size_t len;

    for (unsigned int i = 0; i < ARRAY_LEN; ++i)
    {
        puts("Input a line:");
        if(getline(&two_dim_array[i], &len, stdin) == -1 && ferror(stdin))
        err(1, "getline");
        printf("You've entered %u character(s) (including newline):\n%s",
               strlen(two_dim_array[i]), two_dim_array[i]);
    }


    for (size_t i = 0; i < ARRAY_LEN; ++i)
        free(two_dim_array[i]);

    exit(0);
}
