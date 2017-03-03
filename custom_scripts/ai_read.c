#include <stdio.h>
#include "../MedIOEx/pmedex.h"  // This path should be set properly.
#include <bcm2835.h>

int to_pin(int var) {
	int result;
	switch(var) {
		case 1: result = pe2a_GPIO_J13_1; break;
		case 2: result = pe2a_GPIO_J13_2; break;
		case 3: result = pe2a_GPIO_J13_3; break;
		case 4: result = pe2a_GPIO_J13_4; break;
		default: result = -1;
	}
	return result;
}


int main(int argc, char **argv ){
	if(argc < 2){
		printf("Missing pin number");
		return 1;
	}
	int pin_number = to_pin(atoi(argv[1]));
	pe2a_AI_init();
	printf("%d", pe2a_AI_getVal(pin_number));
	pe2a_bcm2835_close();
}
