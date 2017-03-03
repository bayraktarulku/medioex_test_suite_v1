# MedIOEx Test Suite

## Installation

Normally, you need to install MedIOEx libs from its original repository which can be found [here](https://github.com/pe2a/MedIOEx).
But you won't need it because our installation script will do that for you.

Here are the steps you should follow to install test suite to your Raspberry Pi:

```
# ssh into your Raspberry Pi
$ git clone https://github.com/nejdetckenobi/medioex_test_suite`
$ cd medioex_test_suite`
$ sudo su`
root$ bash install.sh
root$ python3 run.py
```

Then go to your browser and type your Raspberry Pi's local IP with port 5000.

You'll see the main screen that writes/reads every IO slot.
Note that even if you stop the server, **output voltages will be active**.

So for your own safety, write 0 to every possible output slot (especially for relay slots).
