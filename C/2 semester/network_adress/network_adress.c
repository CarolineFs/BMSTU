/* В файл заносится информация в формате
 * xxx.xxx.xxx.xxx/xx
 * Написать функцию для вычисления начального сетевого адреса
 */

#include <stdio.h>
#define FILENAME "/home/bellatrix/Desktop/ip.txt"
#define ARRAY_SIZE 32

void write_in_file();
int input_error_preventer();
void find_adress();
int* mask_array();

int main()
{
    write_in_file();
    find_adress();
    return 0;
}


int* mask_array(int mask, int* mask_a)
{
    for (int i = 0; i < ARRAY_SIZE; ++i)
    {
        if (i < mask)
            mask_a[i] = 1;
        else
            mask_a[i] = 0;
    }
    return mask_a;
}


void find_adress()
{
    FILE *f;
    int mask_a[ARRAY_SIZE], ip[ARRAY_SIZE], adress[ARRAY_SIZE];

    int oct1, oct2, oct3, oct4, mask;

    f = fopen(FILENAME, "r");
    if (f != NULL)
    {
        while (!feof(f))
        {
            fscanf(f, "%d.%d.%d.%d/%d\n", &oct1, &oct2, &oct3, &oct4, &mask);
        }

        mask_array(mask, mask_a);
    }
    else
    {
        printf("Unable to open file.\n");
    }
    fclose(f);
}


void write_in_file()
{
    FILE *f;
    char pos_resp = 'y';
    char response = 'y';
    int oct1, oct2, oct3, oct4, mask;

    f = fopen(FILENAME, "w");
    if (f != NULL)
    {
        while (response == pos_resp)
        {

            printf("Inpit first octet: ");
            oct1 = input_error_preventer();
            while ((oct1 < 0) || (oct1 > 255))
            {
                printf("Wrong value! Try again: ");
                oct1 = input_error_preventer();
            }

            printf("Inpit second octet: ");
            oct2 = input_error_preventer();
            while ((oct2 < 0) || (oct2 > 255))
            {
                printf("Wrong value! Try again: ");
                oct2 = input_error_preventer();
            }

            printf("Inpit third octet: ");
            oct3 = input_error_preventer();
            while ((oct3 < 0) || (oct3 > 255))
            {
                printf("Wrong value! Try again: ");
                oct3 = input_error_preventer();
            }

            printf("Inpit forth octet: ");
            oct4 = input_error_preventer();
            while ((oct4 < 0) || (oct4 > 255))
            {
                printf("Wrong value! Try again: ");
                oct4 = input_error_preventer();
            }

            printf("Inpit mask: ");
            mask = input_error_preventer();
            while ((mask < 0) || (mask > 32))
            {
                printf("Wrong value! Try again: ");
                mask = input_error_preventer();
            }

            fprintf(f, "%d.%d.%d.%d/%d\n", oct1, oct2, oct3, oct4, mask);

            printf("Do you want to continue? y/n: ");
            scanf("\n");
            scanf("%c", &response);
        }

    }
    else
    {
        printf("Unable to open file.\n");
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
