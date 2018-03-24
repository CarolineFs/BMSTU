/* Функция для записи в файл информации о книге:
 * название книги, год издания, количество копий.
 * Функция для чтения информации из файла и вывода на экран.
 * Функция для вывода информации о книге с самым длинным названием
 * и с самым ранним годом издания.
 * Название книги макс 20 символов. */

#include <stdio.h>
#define MAX_TITLE_LEN 20

int input_error_preventer();


int main()
{
    FILE *f;
    char filename[] = "test.txt";
    char pos_resp[] = "y";
    char* title[MAX_TITLE_LEN];
    int copies, year;
    char response[] = "y";

    f = fopen(filename, "a");
    if (f != NULL)
    {
        while (strcmp(response, pos_resp) == 0)
        {
            printf("Input the title of the book: ");
            scanf("\n");
            fgets(title, MAX_TITLE_LEN, stdin);

            printf("Input the number of copies sold: ");
            copies = input_error_preventer();
            while (copies <= 0)
            {
                printf("Incorrect input!\n");
                copies = input_error_preventer();
            }

            printf("Input the the year of publishing: ");
            year = input_error_preventer();
            while ((year <= 0) || (year > 2018))
            {
                printf("Incorrect input!\n");
                year = input_error_preventer();
            }

            fputs(title, f);
            fputc(' ', f);
            fputs(copies, f);
            fputc(' ', f);
            fputs(year, f);
            fputc('\n', f);

            printf("Do you want to continue? y/n: ");
            scanf("%c", &response);
        }


    }
    else
    {
        printf("Unable to open file.\n");
        fclose(f);
    }
    fclose(f);

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

