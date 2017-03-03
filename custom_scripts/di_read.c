#include <stdio.h>
#include "../MedIOEx/pmedex.h"  // This path should be set properly.
#include <bcm2835.h>
#include <stdlib.h>

int to_pin(int var) {
	int result = -1;
	switch(var) {
		case 1: result = pe2a_GPIO_J17_1; break;
		case 2: result = pe2a_GPIO_J17_2; break;
		case 3: result = pe2a_GPIO_J17_3; break;
		case 4: result = pe2a_GPIO_J17_4; break;
		case 5: result = pe2a_GPIO_J16_5; break;
		case 6: result = pe2a_GPIO_J16_6; break;
		case 7: result = pe2a_GPIO_J16_7; break;
		case 8: result = pe2a_GPIO_J16_8; break;
		case 9: result = pe2a_GPIO_J15_9; break;
		case 10: result = pe2a_GPIO_J15_10; break;
		case 11: result = pe2a_GPIO_J15_11; break;
		case 12: result = pe2a_GPIO_J15_12; break;
		case 13: result = pe2a_GPIO_J14_13; break;
		case 14: result = pe2a_GPIO_J14_14; break;
		case 15: result = pe2a_GPIO_J14_15; break;
		case 16: result = pe2a_GPIO_J14_16; break;
		default: result = -1;
	}
	return result;
}


int main(int argc, char** argv) {
	if (argc < 2) {
		printf("Missing pin number\n");
		return 0;
	}
	int pin_number = to_pin(atoi(argv[1]));
	pe2a_DO_DI_init();
	printf("%d", pe2a_DI_getVal(pin_number));
	pe2a_bcm2835_close();
	return 0;
}

