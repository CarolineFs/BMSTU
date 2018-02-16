#include <stdio.h>

float* mm_to_sm_m(float *cm_m, float mm)
{
    cm_m[0] = mm/10;
    cm_m[1] = cm_m[0]/100;
    return cm_m;
}

int main()
{
    float millimeters;
    float cm_m[2];

    printf("Input millimeters: ");
    scanf("%f", &millimeters);

    if (millimeters < 0)
        printf("Incorrect input. ");
    else
    {
        mm_to_sm_m(cm_m, millimeters);
        printf("%f m, %f cm.", cm_m[1], cm_m[0]);

    }

    return 0;
}
