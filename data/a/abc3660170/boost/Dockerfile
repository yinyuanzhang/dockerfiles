FROM abc3660170/gcc:latest
WORKDIR /usr/local/src
RUN wget -O boost_1_62_0.tar.gz http://pilotfiber.dl.sourceforge.net/project/boost/boost/1.62.0/boost_1_62_0.tar.gz
RUN tar -xzvf boost_1_62_0.tar.gz
WORKDIR /usr/local/src/boost_1_62_0
RUN ./bootstrap.sh --with-icu --with-libraries=all
RUN ./b2 threading=multi; exit 0
RUN ./b2 install; exit 0
RUN echo "/usr/local/lib" >> /etc/ld.so.conf
RUN ldconfig
RUN rm -rf /usr/local/src/boost_1_62_0*