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
C_CODE_FILES=$(ls -I OKUBENI custom_scripts)

if [ ! -d "bin" ]
then
    echo "Creating directory for binaries."
    mkdir "bin"
fi

for f in $C_CODE_FILES
do
    echo "Compiling $f"
    (cd "custom_scripts" && gcc -o "../bin/${f%??}" "$f" ../MedIOEx/pmedex.c -lbcm2835 -std=gnu11)
done
