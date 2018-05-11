#include <stdio.h>
#include <string.h>
#define MAX_UNIT_LEN 6

FILE* f;
char* len[9] =    {"mm", "cm", "dm", "km", "Mm", "in", "ft",
                   "yd", "n mile"};
char* time[9] =   {"s", "min", "d", "day", "days", "week",
                   "weeks","month", "months"};
char* weight[6] = {"hg", "mg", "g", "kg", "t", "kt"};
char* amount[9] = {"mm3", "cm3", "dm3", "m3", "l", "ml",
                   "dl", "hl", "Ml"};
char* area[10] =  {"mm2", "cm2", "dm2", "m2", "ha", "km2", "in2"
                   "ft2", "a"};

char unit1[MAX_UNIT_LEN];
char unit2[MAX_UNIT_LEN];

void show_help();

int main()
{
  float q_u2;
  unsigned int error = 0;
  char answer;


  printf("Get help? y/n ");
  scanf("%c", &answer);

  if (answer == 'y')
      show_help();

  printf("Input a string after the pattern: \"how many UNITS in NUMBER UNITS\"\n");
  scanf("\n");

  error = scanf("how many %s in %f %s", unit1, &q_u2, unit2);
  if (error != 3)
    error = scanf("How many %s in %f %s", unit1, &q_u2, unit2);
  if (error != 3)
    error = scanf("how many %s in %f %s?", unit1, &q_u2, unit2);
  if (error != 3)
    error = scanf("How many %s in %f %s?", unit1, &q_u2, unit2);

  if (error != 3)
  {
    printf("Incorrect input!\n");
  }
  if (error == 3)
    printf("OK\n");

}


void show_help()
{
  printf("Posiible length units: \n");
  for (size_t i = 0; i < 9; ++i)
    printf("%s\n", len[i]);

  printf("Posiible time units: \n");
  for (size_t i = 0; i < 9; ++i)
    printf("%s\n", time[i]);

  printf("Posiible weight units: \n");
  for (size_t i = 0; i < 6; ++i)
    printf("%s\n", weight[i]);

  printf("Posiible amount units: \n");
  for (size_t i = 0; i < 9; ++i)
    printf("%s\n", amount[i]);

  printf("Posiible area units: \n");
  for (size_t i = 0; i < 10; ++i)
    printf("%s\n", area[i]);
}
