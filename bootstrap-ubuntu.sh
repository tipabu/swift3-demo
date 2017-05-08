#!/bin/bash
# Pull this entire repo into a fresh VM
set -e -x

REPO="swift3-demo"
TEMPDIR=`mktemp -d -t "bootstrap-$REPO.XXX"`
pushd "$TEMPDIR" >/dev/null

_have() { [ -n "$(type -p $1)" ]; }

if _have git ; then
    tty -s && echo "Using git..."
    git clone "https://github.com/tipabu/$REPO.git" >/dev/null
elif _have curl && _have tar && _have gunzip ; then
    tty -s && echo "Using curl/gunzip/tar..."
    curl -sL "https://github.com/tipabu/$REPO/archive/master.tar.gz" > repo.tar.gz
    gunzip repo.tar.gz >/dev/null
    tar xf repo.tar >/dev/null
    rm repo.tar
    mv "$REPO"{-master,}
elif _have curl && _have unzip ; then
    tty -s && echo "Using curl/unzip..."
    curl -sL "https://github.com/tipabu/$REPO/archive/master.zip" > repo.zip
    unzip repo.zip >/dev/null
    rm repo.zip
    mv "$REPO"{-master,}
else
    echo "*** Install git or curl/tar/gunzip or curl/unzip! ***"
    exit 1
fi
cp -r "$REPO"/* "$REPO"/.[^.]* "$HOME"

popd >/dev/null
rm -rf "$TEMPDIR"

sudo apt-get install -y python-virtualenv libyaml-dev python3 python3-dev python-dev python-tox
( tty -s || [ -t 1 ] ) && echo 'Done!'
