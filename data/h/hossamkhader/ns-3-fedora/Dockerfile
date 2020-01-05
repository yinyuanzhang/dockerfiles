FROM fedora
RUN dnf update -y
RUN dnf install -y git gcc-c++ gdb
RUN git clone https://github.com/hossamkhader/ns-3-dev.git
WORKDIR ns-3-dev
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ./waf configure --enable-examples --enable-tests
RUN ./waf build
