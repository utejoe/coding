/* pg 134 08L06.c: Using shift operators */
#include <stdio.h>

main()
{
	int x, y, z;

	x = 255;
	y = 5;
	printf("Given x = %4d, i.e., 0X%04X\n", x, x);
	printf("      y = %4d, i.e., 0X%04X\n", y, y);
	z = x >> y;
	printf("x >> y	yields: %6d, i.e., 0X%04X\n", z, z);
	z = x << y;
	printf("x << y 	yields: %6d, i.e., 0X%04X\n", z, z);
	return 0;
}
