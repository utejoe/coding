/* 08L04.c: Using the logical negation operator */
#include <stdio.h>

main()
{
	int	num;
	
	num = 7;
	printf("Gibem num = 7\n");
	printf("!(num < 7)    yields: %d\n", !(num < 7));
	printf("!(num > 7)    yields: %d\n", !(num > 7));
	printf("!(num == 7)   yields: %d\n", !(num == 7));
	return 0;
}
