#!/bin/bash

project_name="dogsay"
project_url="https://github.com/botvinick/dogsay/releases/download/1.5.0/dogsay.tar.gz"

if python --version &> /dev/null; then
  if ls $HOME/.$project_name &> /dev/null; then
    python $HOME/.$project_name/main.py
  else
    mkdir $HOME/.$project_name
    curl -fLso $HOME/$project_name.tar.gz $project_url
    tar -xzpf $HOME/$project_name.tar.gz -C $HOME/.$project_name
    rm $HOME/$project_name.tar.gz
    python $HOME/.$project_name/main.py "$@"
  fi
else
  tput bold
  tput setaf 1
  echo "Failed because you don't have Python. Please install Python and try again."
  tput sgr0
fi
