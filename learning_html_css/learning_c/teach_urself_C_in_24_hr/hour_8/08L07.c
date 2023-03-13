/* pg 134 08L07.c: Using the ?: operator */
#include <stdio.h>

main()
{
	int 	x;

	x = sizeof(int);
	printf("%s\n",
		(x == 2)
		? "The int data type has 2 bytes."
		: "int doesn't have 2 bytes.");
	printf("The maximum value of int is: %d\n",
		(x != 2) ? ~(1 << x * 8 - 1) : ~(1 << 15) );
	return 0;
}
