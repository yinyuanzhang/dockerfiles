FROM yunbaoguan/golang-mingw64:latest

RUN wget https://download.libsodium.org/libsodium/releases/libsodium-1.0.16.tar.gz
RUN tar zxf libsodium-1.0.16.tar.gz
RUN cd libsodium-1.0.16 && \
	./configure --host=x86_64-w64-mingw32 --enable-static --prefix=/mingw64 && \
	make && make install && \
	cd ..
RUN rm -r libsodium-1.0.16

RUN wget https://github.com/zeromq/libzmq/releases/download/v4.2.3/zeromq-4.2.3.tar.gz
RUN tar zxf zeromq-4.2.3.tar.gz
RUN cd zeromq-4.2.3 && \
	./configure --host=x86_64-w64-mingw32 --enable-static --prefix=/mingw64 --with-libsodium=/mingw64 && \
	make && make install && \
	cd ..
RUN rm -r zeromq-4.2.3


