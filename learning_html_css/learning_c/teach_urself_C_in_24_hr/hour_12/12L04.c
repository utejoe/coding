/* 12L04.c: Printing out an arra of characters */
#include <stdio.h>

main()
{
 	char array_ch[7] = {'H', 'e', 'l', 'l', 'o', '!', '\0'};
	int i;

	for (i=0; i<7; i++)
           printf("array_ch[%d] contains: %c\n", i, array_ch[i]);
	/*--- method I ---*/
	printf( "Put all elements together(Method I):\n");
	for (i=0; array_ch[i] != '\0' && i<7; i++)
	   printf("%c", array_ch[i]);
	   /*--- mehtod II ---*/
	  printf( "\nPut all elements together(Method II):\n");
	  printf( "%s\n", array_ch);

	  return 0;
} 
