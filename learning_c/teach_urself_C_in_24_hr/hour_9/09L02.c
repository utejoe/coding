/* pg146 09L02.c: Using short and long modifiers */
#include <stdio.h>

main()
{
	printf("The size of short int is: %d.\n", sizeof(short int));
	printf("The size of long int is: %d.\n", sizeof(long int));
	printf("The size of float is: %d.\n", sizeof(float));
	printf("the size of double is: %d.\n", sizeof(double));
	printf("The size of long double is: \n", sizeof(long double));
	return 0;
}
