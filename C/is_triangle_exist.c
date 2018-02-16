#include <stdio.h>
#include <math.h>

int main()
{
    float x[3];
    float y[3];
    float a, b, c;

    for (int i = 0; i < 3; i++)
    {
        printf("Input x: ");
        scanf("%f", &x[i]);

        printf("Input y: ");
        scanf("%f", &y[i]);

    }
    a = sqrt((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]));
    b = sqrt((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]));
    c = sqrt((x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]));

    if ((a + b > c) && (a + c > b) && (b + c > a))
        printf("Triangle exists. ");
    else
        printf("Triangle does not exist. ");

    return 0;
}
