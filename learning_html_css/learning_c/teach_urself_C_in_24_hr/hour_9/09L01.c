/* pg 144 09L01.c: Using signed and unsigned modifiers */
#include <stdio.h>

main()
{
	signed char	ch;
	int		x;
	unsigned int	y;

	ch = 0xFF;
	x = 0xFFFF;
	y = 0xFFFFu;
	printf("The decimal of singned 0xFF is %d.\n", ch);
	printf("The decimal of singned 0xFFFF is %d.\n", x);
	printf("The decimal of unsingned 0xFFFFu is %u.\n", y);
	printf("The hex of decimal 12345 is 0x%X.\n", 12345);
	printf("The hex of decimal -12345 is 0x%X.\n", -12345);
	return 0;
}
