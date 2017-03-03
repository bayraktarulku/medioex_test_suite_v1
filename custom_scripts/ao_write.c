#include <stdio.h>
#include <bcm2835.h>
#include "../MedIOEx/pmedex.h"  // This path should be set properly.
#include <stdlib.h>

int to_pin(int var) {
	int result;
	switch(var) {
		case 1: result = pe2a_GPIO_J1_1; break;
		case 2: result = pe2a_GPIO_J1_2; break;
		case 3: result = pe2a_GPIO_J1_3; break;
		case 4: result = pe2a_GPIO_J1_4; break;
		default: result = -1;
	}
}

int main(int argc, char **argv) {
	if(argc < 3) {
		printf("Missing pin number and/or value");
		return 1;
	}
	int value = atoi(argv[2]);
	if ((0 > value) || (value > 4095)) {
		printf("Invalid value for analog input. Need a value between [0, 4096)");
		return 1;
	}
	int pin_number = to_pin(atoi(argv[1]));
	if(pin_number == -1) {
		printf("Invalid pin number. 1, 2, 3 and 4 are valid.");
		return 1;
	}
	pe2a_AO_init();
	pe2a_AO_writeVal(pin_number, value);
	pe2a_bcm2835_close();
	return 0;
}
