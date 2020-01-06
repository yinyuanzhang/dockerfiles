FROM gcc
#COPY src/doh /usr/src/doh
RUN cd /usr/src && \
    git clone https://github.com/curl/doh.git
WORKDIR /usr/src/doh
RUN make
ENTRYPOINT ["./doh"]
