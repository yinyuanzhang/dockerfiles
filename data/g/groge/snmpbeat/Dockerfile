FROM golang:latest

LABEL maintainer="groge <groge.choi@gmail.com>"

USER root

# Provide a non-root user.
RUN groupadd --gid 1000 beat && \
    useradd --uid 1000 --gid 1000 beat && \
    mkdir -p /home/beat && \
    chown -R beat:beat /home/beat

USER beat

WORKDIR /home/beat

RUN ls -al

RUN git clone https://github.com/isalgueiro/otilio.git

USER root

RUN mkdir -p /usr/local/go/src/github.com/isalgueiro

RUN mv /home/beat/otilio/src/github.com/* /usr/local/go/src/github.com/
RUN mv /home/beat/otilio /usr/local/go/src/github.com/isalgueiro/
RUN ln -s /usr/local/go/src/github.com/isalgueiro/otilio /otilio

USER beat
WORKDIR /otilio
RUN export GOHOME=/usr/local/go
RUN make

# Start pm2.json process file
CMD ["./otilio", "-c", "otilio.yml", "-e", "-d", "\"*\""]
