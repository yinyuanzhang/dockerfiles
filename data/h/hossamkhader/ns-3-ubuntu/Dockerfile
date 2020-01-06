FROM ubuntu
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get -y install git g++ gdb python3
RUN git clone https://github.com/hossamkhader/ns-3-dev.git
WORKDIR ns-3-dev
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ./waf configure --enable-examples --enable-tests
RUN ./waf build
