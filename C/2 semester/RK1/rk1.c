/* Функция принимает на вход натуральное число и определяет сумму первой и послежней цифр
 * Функция, которая для последовательности трехзначных числел определяет значение максимального
 * нечетного элемента и сумму отрицательных чисел. Последовательность оканчивается числом 349
 * Функция, которая считывает из файла txt все числа (int), кратные 7
 */

#include <stdio.h>
#define MAX_FILENAME_LEN 255
#define FILENAME "C:\\Users\\user-lab01\\Documents\\rk1\\nums.txt"
int count_sum(int);
void find_max_and_neg_sum();
void div_by_seven(FILE *f);
int input_error_preventer();

int main()
{
    int number, sum;
    printf("\nSUM\n");
    printf("Input a natural number: ");
    number = input_error_preventer();
    if (number < 10)
        printf("Incorrect innput.\n");
    else
    {
        sum = count_sum(number);
        printf("The sum of first and last digits is: %d.\n", sum);
    }
    find_max_and_neg_sum();

    printf("\nFILE\n");
    FILE *f;
    char filename[MAX_FILENAME_LEN];
    printf("Input the name of the file: ");
    scanf("%s", filename);
    f = fopen(filename, "r");
    if (f != NULL)
    {
        div_by_seven(f);
    }
    else
    {
        printf("Unable to open file.\n");
    }
    fclose(f);
    return 0;
}


void div_by_seven(FILE *f)
{
    _Bool flag = 0;
    printf("Numbers from the file divisible by 7:\n");
    while (!feof(f))
    {
        int cur;
        fscanf(f, "%d\n", &cur);
        if (cur%7 == 0)
        {
            printf("%d\n", cur);
            flag = 1;
        }
    }
    if (!flag)
        printf("No such numbers in the file.\n");
}


void find_max_and_neg_sum()
{
    printf("\nARRAY\n");
    int max = -2, sum = 0, cur;
    while (1)
    {
        printf("Input new element: ");
        cur = input_error_preventer();
        if (cur == 349)
        {
            printf("Ent of the input.");
            break;
        }
        if ((cur < 100) && (cur > -100))
        {
            printf("Ent of the input.");
            break;
        }
        if ((cur < -999) || (cur > 999))
        {
            printf("Ent of the input.");
            break;
        }
        if ((cur % 2 == 1) && (cur > max))
            max = cur;

        if (cur < 0)
            sum += cur;
    }

    if (max == -2)
        printf("No odd elements.\n");
    else
        printf("Maximum odd element: %d.\n", max);
    printf("Sum of the negative elements: %d.\n", sum);
}


int count_sum(int num)
{
    int sum = 0;
    sum += num%10;
    while (num >= 10)
    {
        num /= 10;
    }
    sum += num;

    return sum;
}


int input_error_preventer()
{
    int x, rc;
    char tmp;

    while (((rc = scanf("%d%c", &x, &tmp)) != 2 && rc != EOF) || tmp != '\n')
    {
        printf("Input error. Please, enter a natural number: ");
        do
        {
        rc = scanf("%c", &tmp);
        }
        while(rc != EOF && tmp != '\n');
    }
    return x;
}
