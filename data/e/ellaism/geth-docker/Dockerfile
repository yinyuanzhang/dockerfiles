FROM golang:alpine as builder

# Run and add dependancies. 
ADD apk-build /apk-build
RUN chmod +x /apk-build
RUN /apk-build

# Deploy Ellaism Geth Binary
RUN mkdir -p /go/src/github.com/ellaism/ \
	&& cd /go/src/github.com/ellaism \
	&& wget https://github.com/ellaism/go-ellaism/releases/download/v4.2.1/geth-ellaism-linux.zip \
	&& unzip /go/src/github.com/ellaism/geth-ellaism-linux.zip

FROM golang:1.7	

COPY --from=builder /go/src/github.com/ellaism/geth /go/bin/geth
	
RUN mkdir /blockchain

VOLUME /blockchain

EXPOSE 8545 8546 30303 
EXPOSE 30303/udp 30304/udp

ENTRYPOINT ["/go/bin/geth", "--datadir=/blockchain --rpc"]
