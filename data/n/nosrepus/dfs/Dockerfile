FROM nosrepus/grpc-cpp

RUN apt-get update && \
    apt-get -y install unzip wget

RUN wget https://github.com/libfuse/libfuse/releases/download/fuse-3.0.0/fuse-3.0.0.tar.gz && \
	tar -xzf fuse-3.0.0.tar.gz && \
	cd fuse-3.0.0 && \
	./configure && \
	make && \
	make install