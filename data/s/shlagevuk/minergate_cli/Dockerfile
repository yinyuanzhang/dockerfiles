FROM ubuntu:16.04 

RUN apt-get update \
    && apt-get -qq --no-install-recommends install \
        ca-certificates \
        wget \
	libpcre16-3 \
	libxcb1 \
    && rm -r /var/lib/apt/lists/*

RUN wget -q --content-disposition https://minergate.com/download/deb-cli \
    && dpkg -i *.deb \
    && rm *.deb

ENTRYPOINT ["minergate-cli"]
CMD ["-user", "your.email@gmail.com", "-xmr"]


