/* 05L01.c: Reading input by calling get() */
#include <stdio.h>

main()
{
	int ch;
	printf("Please type in one character: \n");
	ch = getc( stdin );
	printf("The character you just entered is: %c\n", ch);
	return 0;
}
