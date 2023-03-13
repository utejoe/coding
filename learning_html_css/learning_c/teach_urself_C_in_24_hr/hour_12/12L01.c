/* 12L01.c: Initializing an array */
#include <stdio.h>

main()
{
	int i;
	int list_int[1000
	];

	for (i=0; i<10; i++){
	  list_int[i] = i + 1;
	  printf("list_int[%d] is intialized with %d.\n", i, list_int[i]);
	 }
	return 0;
}