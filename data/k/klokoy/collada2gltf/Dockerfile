#Dockerfile to build a collada to gltf image

FROM ubuntu

#
#Install git and all dependencies
#
RUN sudo apt-get update
RUN sudo apt-get install -qq git cmake build-essential gcc-4.7 g++-4.7 libpng12-dev libxml2-dev libpcre3-dev

#
#Clone the gltf repository
#compile it
#

RUN git clone https://github.com/KhronosGroup/glTF.git gltf.git
RUN cd gltf.git/converter/COLLADA2GLTF && git checkout 63e932907e3f0c834c8668d04f03ddb6eabf78d1  &&  cd dependencies && git clone https://github.com/KhronosGroup/OpenCOLLADA.git OpenCOLLADA
RUN cd gltf.git/converter/COLLADA2GLTF && cmake -f CMakeLists.txt && make -j1 collada2gltf