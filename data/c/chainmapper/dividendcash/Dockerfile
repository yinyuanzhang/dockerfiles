FROM chainmapper/walletbase-xenial-build as builder

ENV GIT_COIN_URL    https://github.com/dividendcash/dividendcash.git
ENV GIT_COIN_NAME   dividendcash   

RUN	git clone $GIT_COIN_URL $GIT_COIN_NAME \
	&& cd $GIT_COIN_NAME \
	&& git checkout tags/v1.0.0.0 \
	&& chmod +x autogen.sh \
	&& chmod +x share/genbuild.sh \
	&& chmod +x src/leveldb/build_detect_platform \
	&& ./autogen.sh && ./configure \
	&& make \
	&& make install

FROM chainmapper/walletbase-xenial as runtime

COPY --from=builder /usr/local/bin /usr/local/bin

RUN mkdir /data
ENV HOME /data

#rpc port & main port
EXPOSE 29998 51472

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
RUN chmod 777 /*.sh
CMD /start.sh dividendcash.conf DVD dividendcashd