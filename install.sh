#! /usr/bin/env bash

pip3 install -r requirements.txt

git clone https://github.com/pe2a/MedIOEx
cd MedIOEx
tar zxvf bcm2835-1.50.tar.gz
cd bcm2835-1.50
./configure
make
make check
make install
cd ../..
