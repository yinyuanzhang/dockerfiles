FROM ubuntu

ARG DOICHAIN_VER=master
ARG DOICHAIN_DAPP_VER=master
ENV DOICHAIN_VER $DOICHAIN_VER
ENV DOICHAIN_DAPP_VER $DOICHAIN_DAPP_VER

#Setup run vars
ENV CONFIRM_ADDRESS ""
ENV CONNECTION_NODE 5.9.154.226
ENV DAPP_CONFIRM true
ENV DAPP_DEBUG true
ENV DAPP_DOI_URL http://localhost:3000/api/v1/debug/mail
ENV DAPP_PORT 3000
ENV DAPP_HOST "localhost"
ENV DAPP_SEND true
ENV DAPP_SMTP_USER ""
ENV DAPP_SMTP_HOST ""
ENV DAPP_SMTP_PASS ""
ENV DAPP_SMTP_PORT 587
ENV DAPP_VERIFY true
ENV NODE_PORT 8338
ENV NODE_PORT_TESTNET 18338
ENV NODE_PORT_REGTEST 18445
ENV REGTEST false
ENV TESTNET false
ENV RPC_ALLOW_IP 127.0.0.1
ENV RPC_PASSWORD ""
ENV RPC_PORT 8339
ENV RPC_PORT_TESTNET 18339
ENV RPC_PORT_REGTEST 18332
ENV RPC_USER ""

#Install dependencies
RUN apt-get update && apt-get install -y \
	autoconf \
	apt-utils \
	bsdmainutils \
	build-essential \
	curl \
	jq \
	vim \
	mongodb \
	bc \
	bsdtar \
	dos2unix \
	git \
	libboost-all-dev \
	libevent-dev \
	libssl-dev \
	libtool \
	locales \
	pkg-config \
	sudo \
	&& rm -rf /var/lib/apt/lists/*

RUN export tar='bsdtar'

#Install locales
RUN locale-gen ${OS_LOCALE}

ENV OS_LOCALE en_US.UTF-8
ENV LANG ${OS_LOCALE}
ENV LANGUAGE en_US:en

WORKDIR /
RUN adduser --disabled-password --gecos '' doichain && \
	adduser doichain sudo && \
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER doichain

#Install berkeley-db
WORKDIR /tmp/build/bdb
ADD http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz db-4.8.30.NC.tar.gz
RUN echo '12edc0df75bf9abd7f82f821795bcee50f42cb2e5f76a6a281b85732798364ef  db-4.8.30.NC.tar.gz' | sudo sha256sum -c && \
	sudo tar xzvf db-4.8.30.NC.tar.gz && \
	cd db-4.8.30.NC/build_unix/ && \
	sudo ../dist/configure --enable-cxx && \
	sudo make && \
	sudo make install && \
	sudo ln -s /usr/local/BerkeleyDB.4.8 /usr/include/db4.8 &&\
	sudo ln -s /usr/include/db4.8/include/* /usr/include &&\
	sudo ln -s /usr/include/db4.8/lib/* /usr/lib

#Install doichain-core
WORKDIR /home/doichain
RUN mkdir .doichain && \
	git clone --branch ${DOICHAIN_VER} https://github.com/Doichain/core.git doichain-core && \
	cd doichain-core && \
	./autogen.sh && \
	./configure --without-gui  --disable-tests  --disable-gui-tests && \
	make && \
	sudo make install

RUN sudo curl https://install.meteor.com/ | sh && \
	sudo git clone --branch ${DOICHAIN_DAPP_VER} https://github.com/Doichain/dApp.git /home/doichain/dapp && \
	sudo chown -R doichain:doichain /home/doichain/dapp
WORKDIR /home/doichain/dapp/
RUN meteor npm install && \
	git submodule init && git submodule update && \
	meteor npm install --save bcrypt

#Copy start scripts
WORKDIR /home/doichain/scripts/
COPY entrypoint.sh entrypoint.sh
COPY start.sh start.sh
COPY getblocktimes.sh getblocktimes.sh
COPY doichain-start.sh doichain-start.sh
COPY dapp-start.sh dapp-start.sh

RUN sudo dos2unix \
	entrypoint.sh \
	start.sh \
	doichain-start.sh && \
	sudo chmod +x \
	entrypoint.sh \
	start.sh \
	doichain-start.sh \
	getblocktimes.sh \
	dapp-start.sh && \
	sudo apt-get --purge remove -y dos2unix && \
	sudo rm -rf /var/lib/apt/lists/*

#Create data dir
WORKDIR /home/doichain
RUN mkdir data && \
	cd data && \
	mkdir doichain &&\
	mkdir -p \
	dapp/local && \
	sudo rm -rf \
	/home/doichain/.doichain \
	/home/doichain/dapp/.meteor/local && \
	sudo ln -s /home/doichain/data/doichain /home/doichain/.doichain && \
	sudo ln -s /home/doichain/data/dapp/local /home/doichain/dapp/.meteor

#Run entrypoint
WORKDIR /home/doichain
ENTRYPOINT ["scripts/entrypoint.sh"]

#Start doichain and meteor
CMD ["scripts/start.sh"]

#Expose ports
EXPOSE $DAPP_PORT $NODE_PORT $RPC_PORT
