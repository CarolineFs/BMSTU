#include <stdio.h>

int main(void) 
{
	int r;
	float s;
	const float pi = 3.14;
	
	scanf("%d", &r);
	
	s = pi*r*r;
	printf("Площадь = %f", s);
	return 0;
}
