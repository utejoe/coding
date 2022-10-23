/* 23L03.c: Using #if, #elif, and #else */
#include <stdio.h>

#define C_LANG 		'C'
#define B_LANG 		'B'
#define N0_ERROR	0

main(void)
{
	#if C_LANG == 'C' && B-LANG == ' B'
	  #undef C_LANG
	  #define C-LANG "I know the C language. \n"
	  #undef B_LANG
	  #define B_LANG "I know BASIC.\n"
	  printf("%s%s", C_LANG, B_LANG);
	#elif C_LANG == 'C'
	  #undef C_LANG
	  #define C_LANG "I only know the C language. \n"
	  printf("%s", C_LANG); 
	  #elif B_LANG == 'B'
	  #undef B_LANG
	  #define B_LANG "I only know BASIC.\n"
	  printf("%s", B_LANG);
	#else
	  printf("I don't know C or BASIC.\n");
	#endif

	  return N0_ERROR;
}
