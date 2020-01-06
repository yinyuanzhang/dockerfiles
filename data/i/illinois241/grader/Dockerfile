FROM ubuntu:16.04

# update sources
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:jonathonf/python-3.6 && \
    add-apt-repository ppa:george-edison55/cmake-3.x && \
    apt-get update

# install python3.6
RUN apt-get install -y python3.6 python3-pip python-dev python3.6-dev cmake && \
    rm /usr/bin/python3 && \
    ln -s python3.6 /usr/bin/python3

# install bulid-related tools
RUN apt-get install -y \
        clang=1:3.8-33ubuntu3.1 \
        libncurses5-dev=6.0+20160213-1ubuntu1 \
    	rpcbind \
        valgrind=1:3.11.0-1ubuntu4.2 && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install pexpect psutil stopit

ADD autograder/ autograder

# needed util we refactor all utils imports to be autograder.utils
RUN ln -s autograder/utils utils

# needed until we refactor out utils_py3 in testers
RUN ln -s autograder/utils utils_py3

ENTRYPOINT ["python3", "-m", "autograder"]
