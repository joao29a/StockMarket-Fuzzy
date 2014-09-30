#!/bin/bash

sudo su
wget http://www.antlr3.org/download/Python/antlr_python_runtime-3.1.3.zip
unzip antlr_python_runtime-3.1.3.zip
cd antlr_python_runtime-3.1.3
python setup.py install
cd ..
apt-get install subversion
svn checkout svn://svn.code.sf.net/p/pyfuzzy/code/trunk pyfuzzy-code
cd pyfuzzy-code/pyfuzzy
python setup.py install
cd
echo "acabou"
