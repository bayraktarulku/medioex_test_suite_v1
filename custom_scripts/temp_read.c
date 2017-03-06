#include <stdio.h>
#include "../MedIOEx/pmedex.h"
#include <bcm2835.h>

int main(){
	double val;
	pe2a_getTemperature_init();
	val = pe2a_getTemperature(1);
	printf("%lf", val);
	pe2a_bcm2835_close();
}
