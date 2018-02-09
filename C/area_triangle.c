#include <stdio.h>
#include <math.h>

int main(void) 
{
	
	float x1, y1, x2, y2, x3, y3, s, a, b, c, p;
	
	scanf("x1 = %f", &x1);
	scanf("y1 = %f", &y1);
	scanf("x2 = %f", &x2);
	scanf("y2 = %f", &y2);
	scanf("x3 = %f", &x3);
	scanf("y3 = %f", &y3);
	
	a = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
	b = sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3));
	c = sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
	
	p = (a + b + c)/2;
	
	s = sqrt(p*(p-a)*(p-b)*(p-c));
	
	printf("Площадь = %f", s);
	
	return 0;
}
