FROM kysxd/boost-cpp-container

RUN apt-get update -y && apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

RUN wget -O cmake-3.12.3.tar.gz https://cmake.org/files/v3.12/cmake-3.12.3.tar.gz
RUN tar xzvf cmake-3.12.3.tar.gz
RUN cd cmake-3.12.3 && ./configure && make && make install

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

CMD ["bash"]
