#include <stdio.h>
#include <math.h>
#define EMPTY_FILTERED_ARRAY_CODE -2
#define CONST_CAST(x) (int*) x

int key(const int *pbSrc, const int *peSrc, int **pbDst, int **peDst)
{
  const int *pCurrent = pbSrc;
  const int *min = pbSrc;
  const int *max = pbSrc;

  while(pCurrent != peSrc)
  {
    if (*pCurrent < *min) min = pCurrent;
    if (*pCurrent > *max) max = pCurrent;
    pCurrent++;
  }
  if (abs(min - max) <= 1) return EMPTY_FILTERED_ARRAY_CODE;

  int range = max - min;

  if (range < 0)
  {
    *pbDst = CONST_CAST(max) + 1;
    *peDst = CONST_CAST(min);
  }
  else
  {
    *pbDst = CONST_CAST(min) + 1;
    *peDst = CONST_CAST(max);
  }

  return 0;
}
