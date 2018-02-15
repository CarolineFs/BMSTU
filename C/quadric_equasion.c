#include <stdio.h>
#include <math.h>

void solve_quadric_equasion(float a, float b, float c)
{
    float x1, x2, d;
    if (a == 0)
    {
        if (b != 0)
        {
            x1 = -c/b;
            printf("x = %f", x1);
        }
        else
        {
            if (c == 0)
                printf("x can be every real number.");
            else
                printf("No solutions.");
        }
    }
    else
    {
        d = b*b - 4*a*c;
        if (d > 0)
        {
            x1 = (-b + sqrt(d))/(2*a);
            x2 = (-b - sqrt(d))/(2*a);
            printf("x1 = %f", x1);
            printf("x2 = %f", x2);
        }
        else if (d < 0)
            printf("No real roots. ");
        else
        {
            x1 = -b/(2*a);
            printf("x = %f \n", x1);
        }
    }
}

int main()
{
    float a, b, c;

    printf("Input a: ");
    scanf("%f", &a);

    printf("Input b: ");
    scanf("%f", &b);

    printf("Input c: ");
    scanf("%f", &c);

    solve_quadric_equasion(a, b, c);

    return 0;
}
