FROM alpine:3.8

# Prepare enviroment
RUN apk add curl gcc make g++ libssl1.0 openssl-dev libstdc++

# Build from lastest Github repo
RUN mkdir /simc
RUN curl -L https://api.github.com/repos/simulationcraft/simc/tarball | tar xzpv -C /simc --strip 1
RUN make -C /simc/engine OPENSSL=1 optimized

# add API key
RUN echo "d2jpcd63smepce6wzupkdhecbnffvdmg" > $HOME/.simc_apikey

# Move into right path
RUN mv /simc/engine/simc /bin/simc
RUN rm -rf /simc

# clean up
#RUN apk del curl gcc make g++ openssl-dev
RUN rm -rf /var/cache/apk/*


VOLUME /profiles
VOLUME /outputs

ENTRYPOINT ["/bin/simc"]
