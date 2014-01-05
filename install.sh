#!/bin/sh

if [ "$1" == "" ];then
 DIR=.
else
 DIR=$1
fi

echo Installing into $DIR...
pushd .

virtualenv $DIR
cd $DIR
. ./bin/activate
pip install msgpack-python
git clone https://github.com/tonysimpson/nanomsg-python.git
cd nanomsg-python
python setup.py install

popd
