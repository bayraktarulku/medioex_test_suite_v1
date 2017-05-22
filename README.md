# MedIOEx Test Suite

## Installation

![medioex](https://cloud.githubusercontent.com/assets/4905664/24248008/589a1c9a-0fd6-11e7-810e-7867a606b1c4.gif)


Normally, you need to install MedIOEx libs from its original repository which can be found [here](https://github.com/pe2a/MedIOEx).
But you won't need it because our installation script will do that for you.

Here are the steps you should follow to install test suite to your Raspberry Pi:

```
# ssh into your Raspberry Pi
$ git clone https://github.com/nejdetckenobi/medioex_test_suite
$ cd medioex_test_suite
$ chmod +x install.sh
$ sudo su
root$ ./install.sh
root$ python3 run.py
```

Then go to your browser and type your Raspberry Pi's local IP with port 5000.
(Default username and password are `admin`. You can change them from `config.py`.)
You'll see the main screen that writes/reads every IO slot.
Note that even if you stop the server, **output voltages will be active**.

So for your own safety, write 0 to every possible output slot (especially for relay slots).

To use the Python3 extension for MedIOEx, you can use the links below. 

https://github.com/bayraktarulku/pymedioex
https://github.com/nejdetckenobi/pymedioex
