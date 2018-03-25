/* Функция для записи в файл информации о книге:
 * название книги, год издания, количество копий.
 * Функция для чтения информации из файла и вывода на экран.
 * Функция для вывода информации о книге с самым длинным названием
 * и с самым ранним годом издания.
 * Название книги макс 20 символов. */

#include <stdio.h>
#define MAX_TITLE_LEN 20
#define CURRENT_YEAR 2018

int input_error_preventer();
void write_in_file(char*);
void output_from_file(char*);
void the_longest_title(char*);
void the_earliest_year(char*);

int main()
{
    //char filename[] = "/home/bellatrix/Desktop/git/iu7-cprog-labs-2018-ovchinnikovaanastasia/lab_seminar/working_with_files/test.txt";
    char filename[] = "C:\\Users\\novoc\\Desktop\\test.txt";
    write_in_file(filename);
    output_from_file(filename);
    the_longest_title(filename);
    the_earliest_year(filename);

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


void write_in_file(char* filename)
{
    FILE *f;
    char pos_resp[] = "y";
    int copies, year;
    char response[] = "y";

    f = fopen(filename, "w");
    if (f != NULL)
    {

        while (strcmp(response, pos_resp) == 0)
        {
            char title[MAX_TITLE_LEN];

            fflush(stdin);

            printf("Input the title of the book: ");
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
            while ((year <= 0) || (year > CURRENT_YEAR))
            {
                printf("Incorrect input!\n");
                year = input_error_preventer();
            }

            fputs(title, f);
            fprintf(f, " %d", copies);
            fprintf(f, " %d\n", year);

            printf("Do you want to continue? y/n: ");
            scanf("%c", &response);
        }


    }
    else
    {
        printf("Unable to open file.\n");
    }
    fclose(f);
}


void output_from_file(char* filename)
{
    FILE* f;
    f = fopen(filename, "r");
    char *title[MAX_TITLE_LEN];
    int copies, year;

    if (f != NULL)
    {
        printf("Information from the file: ");
        while (!feof(f))
        {
            fgets(title, MAX_TITLE_LEN, f);
            fscanf(f, " %d %d\n", &copies, &year);
            printf("\nThe name of the book: ");
            fputs(title, stdout);
            printf("The year of publishing: %d\n", year);
            printf("The number of copies sold: %d\n", copies);
        }
    }
    else
    {
        printf("Unable to open file.\n");
    }

    fclose(f);
}


void the_longest_title(char* filename)
{
    FILE* f;
    f = fopen(filename, "r");
    char* longest_title;
    char title[MAX_TITLE_LEN];
    int copies, year;


    if (f != NULL)
    {
        while (!feof(f))
        {
            fgets(title, MAX_TITLE_LEN, f);
            fscanf(f, " %d %d\n", &copies, &year);
            if (sizeof(title)/sizeof(char) >
                 sizeof(longest_title)/sizeof(char))
                    longest_title = title;
        }
        printf("\nThe book with the longest title: ");
        fputs(longest_title, stdout);
    }
    else
    {
        printf("Unable to open file.\n");
    }

    fclose(f);
}


the_earliest_year(char* filename)
{
    FILE* f;
    f = fopen(filename, "r");
    char* earliest_title;
    char title[MAX_TITLE_LEN];
    int copies, year, earliest_year = CURRENT_YEAR, earliest_copies;


    if (f != NULL)
    {
        while (!feof(f))
        {
            fgets(title, MAX_TITLE_LEN, f);
            fscanf(f, " %d %d\n", &copies, &year);
            if (year <= earliest_year)
            {
                earliest_copies = copies;
                earliest_year = year;
                earliest_title = title;
            }
        }
        printf("\nThe book with the year of publishing: \n");
        printf("Name: ");
        fputs(earliest_title, stdout);
        printf("The number of copies sold: %d\n", earliest_copies);
        printf("The year of publishing: %d\n", earliest_year);
    }
    else
    {
        printf("Unable to open file.\n");
    }

    fclose(f);
}
