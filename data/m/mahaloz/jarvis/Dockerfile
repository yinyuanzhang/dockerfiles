#base for building
from ubuntu:xenial
maintainer zbasque@asu.edu

user root

#important libraries
run dpkg --add-architecture i386
run apt-get update && apt-get install -y virtualenvwrapper python2.7-dev build-essential libxml2-dev libxslt1-dev git libffi-dev cmake libreadline-dev libtool debootstrap debian-archive-keyring libglib2.0-dev libpixman-1-dev libqt4-dev graphviz-dev binutils-multiarch nasm libc6:i386 libgcc1:i386 libstdc++6:i386 libtinfo5:i386 zlib1g:i386 vim python-pip libssl-dev

#install PDF -> Text
run git clone https://github.com/euske/pdfminer.git
#run cd pdfminer
#run python setup.py install

#install Text -> Summary
run pip install pyteaser

#install Speech -> Text
run pip install SpeechRecognition
