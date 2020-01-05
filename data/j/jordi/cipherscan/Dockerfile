FROM jordi/ubuntu
MAINTAINER Jordi Íñigo Griera

RUN apt-get update
RUN apt-get -y install git-core python bsdmainutils curl python-six

WORKDIR /git
RUN git clone https://github.com/jvehent/cipherscan.git
WORKDIR /git/cipherscan
RUN git clone --depth=1 https://github.com/tomato42/tlslite-ng.git .tlslite-ng
RUN ln -s .tlslite-ng/tlslite tlslite
RUN git clone --depth=1 https://github.com/warner/python-ecdsa.git .python-ecdsa
RUN ln -s .python-ecdsa/src/ecdsa ecdsa

ENTRYPOINT ["/git/cipherscan/cipherscan"]
CMD ["--help"]
