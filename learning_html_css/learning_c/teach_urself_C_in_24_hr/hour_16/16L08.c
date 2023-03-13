/* 16L08.c: Pointing to a function */
#include <stdio.h>
/* function declaration */
int StrPrint(char *str);
/* main() function */
main()
{
	char str[24] = "Pointing to a function.";
	int (*ptr)(char *str);

	ptr = StrPrint;
	if (!(*ptr)(str))
		printf("Done!\n");

	return 0;
}
/* function definition */
int StrPrint(char *str)
{
	printf("%s\n", str);
	return 0;
}
