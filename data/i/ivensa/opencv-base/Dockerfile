#Version 1.0

FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build

#Update apt-get
RUN apt-get -y update
RUN apt-get -y upgrade

## Install dependencies
RUN apt-get -y install build-essential
RUN apt-get -y install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

# Create directory for installation
RUN mkdir install
WORKDIR /install

# Download OpenCV
RUN git clone https://github.com/opencv/opencv.git
RUN git clone https://github.com/opencv/opencv_contrib.git
RUN git clone https://github.com/shimat/opencvsharp.git
WORKDIR /install/opencvsharp
RUN git fetch --all --tags --prune

#Create build folder for OpenCV
WORKDIR /install/opencv/
RUN mkdir build
WORKDIR /install/opencv/build

#Build OpenCV
RUN cmake .. \
	-D CMAKE_BUILD_TYPE=Release \
	-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_DOCS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_opencv_java=OFF \
    -D BUILD_opencv_python=OFF ..
RUN make -j$(grep -c ^processor /proc/cpuinfo)
RUN make install -j8
RUN ldconfig

# Install the Extern lib.
WORKDIR /install/opencvsharp/
RUN mkdir make
WORKDIR /install/opencvsharp/make
RUN cmake -D CMAKE_INSTALL_PREFIX=/install/opencvsharp/make /install/opencvsharp/src
RUN make -j$(grep -c ^processor /proc/cpuinfo)
RUN make install -j8
RUN ldconfig


WORKDIR /src
RUN cp /install/opencvsharp/make/OpenCvSharpExtern/libOpenCvSharpExtern.so .
RUN git clone https://github.com/shimat/opencvsharp.git

# Install Build the C# part of OpenCvSharp
WORKDIR /src/opencvsharp/src/OpenCvSharp
RUN dotnet restore
RUN dotnet build -c Release -f netstandard2.0 

WORKDIR /src/opencvsharp/src/OpenCvSharp.Blob
RUN dotnet restore
RUN dotnet build -c Release -f netstandard2.0 

WORKDIR /src/opencvsharp/src/OpenCvSharp.Extensions
RUN dotnet restore
RUN dotnet build -c Release -f netstandard2.0 

RUN mkdir /src/opencvsharp/build
WORKDIR /src/opencvsharp/build
RUN cp /src/libOpenCvSharpExtern.so .
RUN cp /src/opencvsharp/src/OpenCvSharp/bin/Release/netstandard2.0/* .
RUN cp /src/opencvsharp/src/OpenCvSharp.Blob/bin/Release/netstandard2.0/* .
RUN cp /src/opencvsharp/src/OpenCvSharp.Extensions/bin/Release/netstandard2.0/* .
RUN cp /install/opencv/build/lib/* .

# docker buildx build --platform linux/amd64 --rm -f "Dockerfile" -t ivensa/opencv-base:latest --push .