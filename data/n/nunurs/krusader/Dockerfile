  
FROM djaydev/krusader:latest
RUN apk add --no-cache make
RUN wget http://www.rarlab.com/rar/rarlinux-5.7.1.tar.gz && \
	tar -xzvf rarlinux-5.7.1.tar.gz && \
	cd rar && \
	make && \
	mv rar /usr/local/bin/rar


