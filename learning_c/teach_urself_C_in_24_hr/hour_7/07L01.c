/* 07L01.c: Using a while loop */
#include <stdio.h>

main()
{
	int c;

	c = ' ';
	printf("Enter a character:\n(enter x to exit)\n");
	while (c != 'x') {
		c = getc(stdin);
		putchar (c);
	}
	printf("\nOut of the while looo. Bye!\n");
	return 0;
}
