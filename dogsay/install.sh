#!/bin/bash

now=$(date +"%s")
cwd=$(pwd)
rm -f /usr/local/bin/dogsay
rm -f /usr/local/bin/dogsay.py
cd $HOME
mkdir dogsay_$now
cd dogsay_$now
curl -fsLo dogsay.tar.gz https://benbotvinick.com/projects/dogsay/dogsay.tar.gz
tar -xzpf dogsay.tar.gz
rm dogsay.tar.gz
mkdir -p /usr/local/bin
mv dogsay/dogsay /usr/local/bin/dogsay
mv dogsay/dogsay.py /usr/local/bin/dogsay.py
cd ..
rm -rf dogsay_$now
cd $cwd
