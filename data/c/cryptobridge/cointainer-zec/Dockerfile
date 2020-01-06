FROM cryptobridge/baseimage:xenial-build AS build

RUN git clone https://github.com/zcash/zcash.git . && \
  git checkout v2.0.7-3

RUN chmod a+x ./autogen.sh
RUN ./zcutil/fetch-params.sh
RUN ./zcutil/build.sh

FROM cryptobridge/baseimage:xenial

COPY --from=build /build/src/zcashd /usr/local/bin/zcashd
COPY --from=build /build/src/zcash-cli /usr/local/bin/zcash-cli
COPY --from=build /build/zcutil/fetch-params.sh /usr/local/bin/fetch-params
COPY --from=build /root/.zcash-params /home/crypto/.zcash-params

USER crypto
RUN mkdir /home/crypto/.zcash && touch /home/crypto/.zcash/zcash.conf

EXPOSE 8232
CMD ["zcashd"]
