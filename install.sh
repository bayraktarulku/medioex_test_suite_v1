#! /usr/bin/env bash

# bcm2835 install
cd ..
wget https://github.com/pe2a/MedIOEx/raw/master/bcm2835-1.50.tar.gz
tar xvf bcm2835-1.50.tar.gz
cd bcm2835-1.50
./configure
make
make check
make install

# Download a release for medioex
wget https://github.com/nejdetckenobi/pymedioex/archive/py34.tar.gz
tar zxvf py34.tar.gz
(cd pymedioex-py34 & python3 setup.py install)

(cd medioex_test_suite & pip3 install -r requirements.txt)

# Cleaning up
rm -rf bcm2835-1.50*
rm -rf py34*
