#include <stdio.h>
#include "../MedIOEx/pmedex.h"  // This path should be set properly.
#include <bcm2835.h>
#include <stdlib.h>

int to_pin(int var) {
	int result;
	switch(var) {
		case 1: result = pe2a_GPIO_J4_1; break;
		case 2: result = pe2a_GPIO_J4_2; break;
		case 3: result = pe2a_GPIO_J4_3; break;
		case 4: result = pe2a_GPIO_J4_4; break;
		case 5: result = pe2a_GPIO_J5_5; break;
		case 6: result = pe2a_GPIO_J5_6; break;
		case 7: result = pe2a_GPIO_J5_7; break;
		case 8: result = pe2a_GPIO_J5_8; break;
		case 9: result = pe2a_GPIO_J6_9; break;
		case 10: result = pe2a_GPIO_J6_10; break;
		case 11: result = pe2a_GPIO_J6_11; break;
		case 12: result = pe2a_GPIO_J6_12; break;
		case 13: result = pe2a_GPIO_J3_1; break; // Relay triggers
		case 14: result = pe2a_GPIO_J3_2; break; // Relay triggers
		case 15: result = pe2a_GPIO_J3_3; break; // Relay triggers
		case 16: result = pe2a_GPIO_J3_4; break; // Relay triggers
	}
	return result;
}


int main(int argc, char** argv) {
	if (argc < 3) {
		printf("Missing pin number and/or pin value\n");
		return 0;
	}
	int pin_number = to_pin(atoi(argv[1]));
	int pin_value = atoi(argv[2]);
	pe2a_DO_DI_init();
	if(pin_value == 1) pe2a_DO_setHigh(pin_number);
	else if(pin_value == 0) pe2a_DO_setLow(pin_number);
	pe2a_bcm2835_close();
	return 0;
}

