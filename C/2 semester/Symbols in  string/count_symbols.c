/* Для выбранной строки (пользователь вводит номер)
 * из файла вывести количество гласных и согласных букв;
 * количество слов; наиболее часто повторяющийся символ. */


#include <stdio.h>
#include <string.h>
#define MAX_STRING_LEN 255
#define FILENAME "C:\\Users\\user-lab01\\Desktop\\test.txt"
#define VOVELS "eyuioaуеэоаыяиюё"
#define CONSONANTS "qwrtplkjhgfdszxcvbnmйцкнгшщзхъждлрпвфчсмтьб"


int count_file_strings();
int input_error_preventer();
int get_string_number(int);
void count_vovels_and_cons(int);


int main()
{
    int strings_q;
    strings_q = count_file_strings() - 1;
    if (strings_q == -1)
        printf("Unable to open file.\n");
    else
    {
        if (strings_q == 0)
            printf("The file is empty. \n");
        else
        {
            int string_num;
            string_num = get_string_number(strings_q);
            count_vovels_and_cons(string_num);
        }
    }
    return 0;
}


void count_vovels_and_cons(int str_num)
{
    FILE *f;
    char str[MAX_STRING_LEN];
    f = fopen(FILENAME, "r");
    if (f != NULL)
    {
       int vov = 0, cons = 0;
       while (!feof(f))
       {
           fgets(str, MAX_STRING_LEN, f);
           int *p = str;
           for (size_t i = 0; i < strlen(str); ++i)
           {
               printf("%s", &p);
               ++p;
           }
       }
    }
    else
    {
        printf("Unable to open file.\n");
    }
    fclose(f);

}


int get_string_number(int k)
{
    int num;
    printf("Strings in file: %d, including string 0. ", k);
    printf("Input string number: ");
    num = input_error_preventer();
    while ((num < 0) || (num > k))
    {
        printf("No such string. Try again!");
        num = input_error_preventer();
    }
    return num;
}


int count_file_strings()
{
    FILE *f;
    char str[MAX_STRING_LEN];
    f = fopen(FILENAME, "r");
    if (f != NULL)
    {
        int k = 0;
        while (!feof(f))
        {
            fgets(str, MAX_STRING_LEN, f);
            ++k;
        }
        return k;
    }
    else
    {
        printf("Unable to open file.\n");
        return -1;
    }
    fclose(f);
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
