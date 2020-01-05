FROM bitriseio/android-ndk:v2018_12_29-08_24-b1315

RUN echo "Install pip3" && \ 
sudo apt-get update && \
sudo apt-get -y install python3-pip

RUN echo "Install conan" && \ 
pip3 install conan && \
conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan

RUN echo "Install cmake" && \
cd $HOME && \
wget https://cmake.org/files/v3.11/cmake-3.11.2-Linux-x86_64.tar.gz && \
tar -xzf cmake-3.11.2-Linux-x86_64.tar.gz && \
cp cmake-3.11.2-Linux-x86_64/bin/cmake /usr/local/bin && \
cp -a cmake-3.11.2-Linux-x86_64/share/. /usr/local/share/

RUN echo "Install ninja" && \
apt-get update && apt-get install -y ninja-build

RUN echo "Install ccache" && \
apt-get update && apt-get install -y ccache

RUN echo "Install protobuf" && \
curl -OL https://github.com/google/protobuf/releases/download/v3.6.0/protoc-3.6.0-linux-x86_64.zip && \
unzip protoc-3.6.0-linux-x86_64.zip -d protoc3 && \
sudo mv protoc3/bin/* /usr/local/bin/ && \
sudo mv protoc3/include/* /usr/local/include/

CMD bitrise -version