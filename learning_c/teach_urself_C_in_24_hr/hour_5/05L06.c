/* 05L06.c: Specifying minimum field width (pg83) */
#include <stdio.h>
main()
{
	int num1, num2;
	num1 = 12;
	num2 = 12345;
	printf("%d\n", num1);
	printf("%d\n", num2);
	printf("%5d\n", num1);
	printf("%5d\n", num2);
	printf("%05d\n", num1);
	printf("%2d\n", num2);
	printf("%7d\n", num2);
	printf("%07d\n", num2);
	return 0;
}
