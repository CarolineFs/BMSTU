#include <stdio.h>
#include <locale.h>

void check_coords(float x, float y)
{
    if ((x > 0) && (y > 0))
        printf("Первая");
    else if ((x > 0) && (y < 0))
        printf("Вторая");
    else if ((x < 0) && (y < 0))
        printf("Третья");
    else if ((x < 0) && (y > 0))
        printf("Четвертая");
    // Исправление
    else if ((y == 0) || (x == 0))
        printf("Точка лежит на осях");
    else
        printf("Начало координат");
}

int main()
{
    setlocale(LC_ALL, "Russian");
    float x, y;
    printf("Введите x: ");
    scanf("%f", &x);

    printf("Введите y: ");
    scanf("%f", &y);
    check_coords(x, y);

    return 0;
}
