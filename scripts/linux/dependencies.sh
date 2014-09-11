#!/bin/bash

has_python_pip=false;
has_quandl=false;
has_pandas=false;

check_dependencies(){
  echo "Checking dependencies..."
  dpkg -l  | grep -i python-pip
  if [ $? -ne 0 ]; then
    echo "python-pip not found."
  else
    has_python_pip=true;
    pip freeze | grep -i quandl
    if [ $? -ne 0 ]; then
      echo "quandl not found."
    else
      has_quandl=true;
    fi;
    dpkg -l | grep -i python-pandas
    if [ $? -ne 0 ]; then
      pip freeze | grep -i pandas
      if [ $? -ne 0 ]; then
        echo "pandas not found."
      else
        has_pandas=true;
      fi;
    else
      has_pandas=true;
    fi;
  fi;
}

install_dependencies(){
  if [ $has_python_pip == false ]; then
    echo "Installing python-pip..."
    apt-get install python-pip
  fi;
  if [ $has_quandl == false ]; then
    echo "Installing quandl..."
    pip install quandl
  fi;
  if [ $has_pandas == false ]; then
    echo "Installing pandas..."
    pip install pandas
  fi;
  echo "Done."
}

check_dependencies
install_dependencies
