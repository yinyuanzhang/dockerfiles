FROM ubuntu:latest

RUN apt-get update
RUN apt install -y software-properties-common
RUN apt install apt-utils inotify-hookable -y
RUN add-apt-repository -y ppa:jonathonf/gcc-7.3
RUN apt-get update
RUN apt install -y gcc-7 g++-7 git build-essential libbz2-dev cmake libmicrohttpd-dev libuv1-dev libssl-dev wget gcc g++  
RUN apt clean 
RUN rm -rf /var/lib/apt/lists/*


RUN git clone https://github.com/xmrig/xmrig.git
RUN cd xmrig && mkdir build && \
	cd  build && \
	cmake .. -DCMAKE_C_COMPILER=/usr/bin/gcc-7 -DCMAKE_CXX_COMPILER=/usr/bin/g++-7 && \
	make 
	
COPY ./config.json /xmrig/build/config.json
COPY ./run-and-grep.sh /xmrig/build/run-and-grep.sh

RUN chmod +x /xmrig/build/run-and-grep.sh

CMD ["sh","-c","cd xmrig/build/ && ./run-and-grep.sh"]
