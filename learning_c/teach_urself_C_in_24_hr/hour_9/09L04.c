/* pg 149. 09L04.c: Using sin(), cos(), and tan() functions */
#include <stdio.h>
#include <math.h>

main()
{
	double x;

	x = 45.0;				/* 45 degree */
	x *= 3.141593 / 180.0;	/* convert to radians */

	printf("The sine of 45 is:	%f.\n", sine);
	printf("The cosine of 45 is: 	%f.\n", cosine);
	printf("The tangent of 45 is: 	%f.\n", tangent);
	return 0;
}
