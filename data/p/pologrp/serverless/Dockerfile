# Build and install CMake from source
FROM lambci/lambda:build-nodejs8.10 AS cmake
RUN git clone https://gitlab.kitware.com/cmake/cmake.git /tmp/cmake
WORKDIR /tmp/cmake
RUN git checkout -b install v3.13.0
RUN ./configure --no-qt-gui
RUN make
RUN make install

# Build and install 0MQ from source
FROM lambci/lambda:build-nodejs8.10 AS zmq
COPY --from=cmake /usr/local /usr/local
RUN git clone https://github.com/zeromq/libzmq /tmp/libzmq
WORKDIR /tmp/libzmq
RUN git checkout -b install v4.2.5
RUN mkdir build
WORKDIR /tmp/libzmq/build
RUN cmake -D CMAKE_INSTALL_PREFIX=/usr/local  \
          -D CMAKE_BUILD_TYPE=Release         \
          -D ENABLE_DRAFTS=OFF                \
          -D ENABLE_CURVE=OFF                 \
          -D BUILD_TESTS=OFF                  \
          -D BUILD_SHARED=ON                  \
          -D BUILD_STATIC=ON                  \
          -D WITH_OPENPGM=OFF                 \
          -D WITH_DOC=OFF                     \
          -D LIBZMQ_WERROR=OFF                \
          -D LIBZMQ_PEDANTIC=OFF              \
          ../
RUN cmake --build .
RUN cmake --build . --target install

# Build and install OpenBLAS from source
FROM lambci/lambda:build-nodejs8.10 AS openblas
COPY --from=zmq /usr/local /usr/local
RUN git clone https://github.com/xianyi/OpenBLAS /tmp/openblas
WORKDIR /tmp/openblas
RUN git checkout -b install v0.3.3
RUN make NO_LAPACK=0 NO_CBLAS=1
RUN make PREFIX=/usr/local install

# Build and install cereal from source
FROM lambci/lambda:build-nodejs8.10 AS cereal
COPY --from=openblas /usr/local /usr/local
RUN git clone https://github.com/USCiLab/cereal /tmp/cereal
WORKDIR /tmp/cereal
RUN git checkout -b install v1.2.2
RUN mkdir build
WORKDIR /tmp/cereal/build
RUN cmake -D JUST_INSTALL_CEREAL=ON ../
RUN cmake --build . --target install

# Assemble all the built and installed libraries together
FROM lambci/lambda:build-nodejs8.10 AS final
COPY --from=cereal /usr/local /usr/local
WORKDIR /
