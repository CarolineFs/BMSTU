/* В файл заносится информация в формате
 * xxx.xxx.xxx.xxx/xx
 * Написать функцию для вычисления начального сетевого адреса
 */

#include <stdio.h>
#include <math.h>
#define FILENAME "/home/bellatrix/Desktop/ip.txt"
#define ARRAY_SIZE 32
#define OCTET_SIZE 8

void write_in_file();
int input_error_preventer();
void find_adress();
void mask_array();
void ip_array();
void bitwise_multiplication();
int binary_to_decimal();

int main()
{
    write_in_file();
    find_adress();
    return 0;
}


int binary_to_decimal(int* adress, size_t start)
{
    int res = 0, value = 7;
    for (size_t i = start; i < start + 8; ++i)
    {
       res += adress[i]*pow(2, value--);
    }

    return res;
}


void binary_code_array(int* ip, int oct, size_t i)
{
    while (oct > 0)
    {
        ip[i--] = oct % 2;
        oct /= 2;
    }
}


void ip_array(int oct1, int oct2, int oct3, int oct4, int* ip)
{
    binary_code_array(ip, oct4, OCTET_SIZE*4 - 1);
    binary_code_array(ip, oct3, OCTET_SIZE*3 - 1);
    binary_code_array(ip, oct2, OCTET_SIZE*2 - 1);
    binary_code_array(ip, oct1, OCTET_SIZE - 1);
}


void bitwise_multiplication(int* mask_a, int* ip, int* adress)
{
    for (size_t i = 0; i < ARRAY_SIZE; ++i)
        adress[i] = mask_a[i]*ip[i];
}


void mask_array(int mask, int* mask_a)
{
    for (int i = 0; i < mask; ++i)
        mask_a[i] = 1;
}


void find_adress()
{
    FILE *f;
    int mask_a[ARRAY_SIZE] = {0}, ip[ARRAY_SIZE] = {0}, adress[ARRAY_SIZE] = {0};

    int oct1, oct2, oct3, oct4, mask;
    int a_oct1, a_oct2, a_oct3, a_oct4;

    f = fopen(FILENAME, "r");
    if (f != NULL)
    {
        while (!feof(f))
        {
            fscanf(f, "%d.%d.%d.%d/%d\n", &oct1, &oct2, &oct3, &oct4, &mask);
            mask_array(mask, mask_a);
            ip_array(oct1, oct2, oct3, oct4, ip);
            bitwise_multiplication(mask_a, ip, adress);

            a_oct1 = binary_to_decimal(adress, 0);
            a_oct2 = binary_to_decimal(adress, 8);
            a_oct3 = binary_to_decimal(adress, 16);
            a_oct4 = binary_to_decimal(adress, 24);

            printf("\nNetwork adress: %d.%d.%d.%d\n", a_oct1, a_oct2, a_oct3, a_oct4);
        }
    }
    else
    {
        printf("Unable to open file.\n");
    }
    fclose(f);
}


int value_checker(int value, char* message, int comp_lower, int comp_upper)
{
    value = input_error_preventer();
    while ((value < comp_lower) || (value > comp_upper))
    {
        printf(message);
        value = input_error_preventer();
    }
    return value;
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
            oct1 = value_checker(oct1, "Wrong value! Try again: ", 0, 255);

            printf("Inpit second octet: ");
            oct2 = value_checker(oct2, "Wrong value! Try again: ", 0, 255);

            printf("Inpit third octet: ");
            oct3 = value_checker(oct3, "Wrong value! Try again: ", 0, 255);

            printf("Inpit forth octet: ");
            oct4 = value_checker(oct4, "Wrong value! Try again: ", 0, 255);

            printf("Inpit mask: ");
            mask = value_checker(oct1, "Wrong value! Try again: ", 0, 32);

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
