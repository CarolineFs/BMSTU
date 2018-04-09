#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define OPEN_FILE_ERROR_MESSAGE "Unable to open file.\n"
#define FILENAME "C:\\msys64\\home\\novoc\\git\\iu7-cprog-labs-2018-ovchinnikovaanastasia\\lab_03_3\\rand_nums.bin"
#define FLOAT_INPUT_ERROR_MESSAGE "Input error. Pleas input a float or an integer.\n"
#define INT_INPUT_ERROR_MESSAGE "Input error. Pleas input an integer.\n"
#define MAX_NUMBERS_Q 255

int int_input_error_preventer();
void write_random_numbers(int);
void read_file(int,int *num_array);


int main ()
{
  srand(time(NULL));
  int number_of_random_values;
  int num_array[MAX_NUMBERS_Q];
  printf("How many random values should I write in the file? ");
  number_of_random_values = int_input_error_preventer();
  while ((number_of_random_values < 0) || (number_of_random_values > MAX_NUMBERS_Q))
  {
    printf("Incorrect input!\n");
    number_of_random_values = int_input_error_preventer();
  }
  write_random_numbers(number_of_random_values);
  read_file(number_of_random_values, num_array);

  return 0;
}


void read_file(int q, int *num_array)
{
  printf("\nNumbers read from the file:\n");
  setbuf(stdin, NULL);
  FILE *f;
  f = fopen(FILENAME, "rb");
  if (f != NULL)
  {
    for (size_t i = 0; i < q; ++i)
    {
      fread(&num_array[i], sizeof(int), 1, f);
      printf("%d\n", num_array[i]);
    }
  }
  else
  {
    printf(OPEN_FILE_ERROR_MESSAGE);
  }
  fclose(f);

}


void write_random_numbers(int q)
{
  setbuf(stdin, NULL);
  FILE *f;
  f = fopen(FILENAME, "wb");
  if (f != NULL)
  {
    for (int i = 0; i < q; ++i)
    {
      int r;
      int err;
      r = rand();
      err = fwrite(&r, sizeof(int), 1, f);
    }
    printf("The file has been just filled with %d random numbers.\n", q);
  }
  else
  {
    printf(OPEN_FILE_ERROR_MESSAGE);
  }
  fclose(f);
}


int int_input_error_preventer()
{
  float x, rc;
  char tmp;
  while (((rc = scanf("%f%c", &x, &tmp)) != 2 && rc != EOF) || tmp != '\n')
  {
    printf(INT_INPUT_ERROR_MESSAGE);
    do
    {
    rc = scanf("%c", &tmp);
    }
    while(rc != EOF && tmp != '\n');
  }
  return x;
}



