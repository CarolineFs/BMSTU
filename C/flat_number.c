#include <stdio.h>

int count_entrance(const int floors_number,  const int flats_on_floor, int flat_number)
{
    float flats_in_entrance = floors_number * flats_on_floor;
    int entrance;
    for (int ent = 0;; ent += flats_in_entrance)
        if (flat_number <= ent)
        {
           entrance = ent/27 + 1;
           break;
        }
    return entrance;
}

int main()
{
    int flat_number;
    const int floors_number = 9;
    const int flats_on_floor = 3;

    for (;;)
    {
        printf("Input flat number: ");
        scanf("%d", &flat_number);
        if (flat_number <= 0)
            printf("Incorrect input. ");
        else
            break;
    }


    int entrance;
    entrance =  count_entrance(floors_number, flats_on_floor, flat_number);
    entrance -= 1;

    printf("Floor: %d", entrance);

    return 0;
}
