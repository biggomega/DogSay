#!/bin/bash

if python --version ; then
    now=$(date +"%s")
    cwd=$(pwd)
    version="1.0.0"
    rm -rf $HOME/.dogsay
    cd $HOME
    mkdir dogsay_$now
    cd dogsay_$now
    curl -fsLo dogsay.tar.gz https://benbotvinick.com/projects/dogsay/dogsay-$version.tar.gz
    tar -xzpf dogsay.tar.gz
    rm dogsay.tar.gz
    mkdir -p /usr/local/bin
    mv dogsay/dogsay $HOME/.dogsay/bin/dogsay
    mv dogsay/dogsay.py $HOME/.dogsay/dogsay.py
    mv dogsay/update.sh $HOME/.dogsay/update.sh
    touch $HOME/.dogsay/VERSION
    echo "Dogsay $version" > .dogsay/VERSION
    cd ..
    rm -rf dogsay_$now
    cd $cwd
else
    echo "\033[1m\u001b[31mInstallation failed because you don't have Python. Please install Python and try again.\u001b[0m\u001b[0m"
fi
