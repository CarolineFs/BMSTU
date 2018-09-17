#include <malloc.h>
#include <string.h>
#include <memory.h>

void mySort( void * first, size_t number, size_t size, int ( * comparator ) ( const void *, const void * ) )
{
  void* end = first + number * size - size;
  /* Модифицированная сортировка пузырьком 2 */
  for (unsigned int i = 0; i < number; i++)
  {
    if (i & 1)
    {
      for (void* p = first; p != end - size; p += size)
      {
        if (comparator(p, p + size) > 0)
        {
          void* buff = malloc(size);
          memccpy(buff, p, 9, size);
          memmove(p, p+size, size);
          memmove(p+size, buff, size);
          free(buff);
        }
      }
    }
    else
    {
      for (void* p = end; p != (first + size); p -= size)
      {
        if (comparator(p, p - size) < 0)
        {
            void* buff = malloc(size);
            memccpy(buff, p, 9, size);
            memmove(p, p-size, size);
            memmove(p-size, buff, size);
            free(buff);
        }
      }
    }
  }
}
