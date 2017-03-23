#! /usr/bin/env bash

# bcm2835 install
wget https://github.com/pe2a/MedIOEx/blob/master/bcm2835-1.50.tar.gz
tar zxvf bcm2835-1.50.tar.gz
cd bcm2835-1.50
./configure
make
make check
make install
cd ..

# Download a release for medioex
wget https://github.com/nejdetckenobi/pymedioex/archive/py34.tar.gz
tar zxvf py34.tar.gz
cd pymedioex-py34
python3 setup.py install

# Clone test suite
git clone https://github.com/nejdetckenobi/medioex_test_suite
cd medioex_test_suite
pip3 install -r requirements.txt

# Cleaning up
rm -rf bcm2835-1.50*
rm -rf py34*
