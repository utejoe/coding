/* 04L04.c: Integer vs. floating point division */
# include <stdio.h>
main()
{
	int int_num1, int_num2, int_num3; /* Declare integer variables */
	float flt_num1, flt_num2, flt_num3; /*Declare integer variables */
	
	int_num1 = 32/10; /* Both divisor and dividend are integers */
	flt_num1 = 32/10;
	int_num2 = 32.0/10; /* the divisor is an integer */
	flt_num2 = 32.0/10;
	int_num3 = 32/10.0; /* the dividend is an integer */
	flt_num3 = 32/10.0;

	printf("The integer divis. of 32/10 is: %d\n", int_num1);
	printf("The floating-point divis. of 32/10 is: %f\n", flt_num1);
	printf("the integer divis. of 32.0/10 is: %d\n", int_num2);
	printf("the floating-point divis. of 32.0/10 is: %f\n", flt_num2);
	printf("The integer divis. of 32/10.0 is: %d\n", int_num3);
	printf("The floating-point divis. of 32/10.0 is: %f\n", flt_num3);
	return 0;
}
