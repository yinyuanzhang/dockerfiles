FROM amazonlinux:1-with-sources

ARG CMAKE_VERSION=3.14.5
ENV CMAKE_VERSION=${CMAKE_VERSION}

RUN yum install -y gcc gcc-c++ glibc-devel patch wget git zip unzip

RUN wget https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz
RUN tar -xvzf cmake-${CMAKE_VERSION}.tar.gz

RUN (cd cmake-${CMAKE_VERSION}; ./bootstrap)
RUN (cd cmake-${CMAKE_VERSION}; make)
RUN (cd cmake-${CMAKE_VERSION}; make install)

RUN cmake --version

RUN yum install -y make

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

RUN pip install Pillow
RUN pip install unittest-xml-reporting

# RUN yum install -y gcc64-c++ libcurl-devel libjpeg-turbo-devel libpng-devel openssl-devel zlib-devel python34-pip cmake3 jq
# RUN pip install awscli --upgrade

# RUN git clone https://github.com/awslabs/aws-lambda-cpp.git
# RUN (cd aws-lambda-cpp; mkdir build)
# RUN (cd aws-lambda-cpp/build; cmake3 .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=~/out)
# RUN (cd aws-lambda-cpp/build; make && make install)

# RUN git clone https://github.com/aws/aws-sdk-cpp.git
# RUN (cd aws-sdk-cpp; mkdir build)
# RUN (cd aws-sdk-cpp/build; cmake3 .. -DBUILD_ONLY=s3 -DBUILD_SHARED_LIBS=OFF -DENABLE_UNITY_BUILD=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=~/out)
# RUN (cd aws-sdk-cpp/build; make && make install)

CMD ["/bin/bash"]
