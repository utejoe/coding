/* 05L07.c: Aligning output (pg 83) */
#include <stdio.h>
main()
{
	int num1;
	int num2;
	int num3;
	int num4;
	int num5;

	num1 = 1;
	num2 = 12;
	num3 = 123;
	num4 = 1234;
	num5 = 12345;
	printf("%8d  %-8d\n", num1, num1);
	printf("%8d  %-8d\n", num2, num2);
	printf("%8d  %-8d\n", num3, num3);
	printf("%8d  %-8d\n", num4, num4);
	printf("%8d  %-8d\n", num5, num5);
	return 0;
}
