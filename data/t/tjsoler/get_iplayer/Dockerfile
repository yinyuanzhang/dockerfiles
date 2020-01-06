FROM alpine:latest

LABEL version="3.22"
LABEL maintainer="Simon Emms <simon@simonemms.com>"

ARG ATOMIC_PARSLEY_URL="https://bitbucket.org/shield007/atomicparsley/raw/68337c0c05ec4ba2ad47012303121aaede25e6df/downloads/build_linux_x86_64/AtomicParsley"
ARG GET_IPLAYER_URL="https://raw.github.com/get-iplayer/get_iplayer/master/get_iplayer"
ARG GET_IPLAYER_CGI_URL="https://raw.githubusercontent.com/get-iplayer/get_iplayer/master/get_iplayer.cgi"

ARG USER_NAME="get_iplayer"

ENV OUTPUT_DIR=/opt/data
ENV CONFIG_DIR=/opt/config

WORKDIR /opt/get_iplayer

ADD run.sh .
ADD logo.txt .

# Create the user
RUN addgroup -g 1000 ${USER_NAME} \
  && adduser -u 1000 -G ${USER_NAME} -s /bin/sh -D ${USER_NAME}

# Install system dependencies
RUN apk add --no-cache curl

# Get iPlayer dependencies
RUN apk add --no-cache perl-libwww perl-lwp-protocol-https perl-mojolicious perl-xml-libxml \
  && apk add --no-cache ffmpeg \
  && apk add --no-cache perl-cgi \
  && apk add --no-cache perl-fcgi \
  && curl -L -o AtomicParsley ${ATOMIC_PARSLEY_URL} \
  && install -m 755 ./AtomicParsley /usr/local/bin

# Install get_iplayer
RUN curl -LO ${GET_IPLAYER_URL} \
  && install -m 755 ./get_iplayer /usr/local/bin

# Install get_iplayer web gui
RUN curl -LO ${GET_IPLAYER_CGI_URL} \
  && install -m 755 ./get_iplayer.cgi /usr/local/bin

# Clean up after ourselves
RUN rm ./AtomicParsley \
  && rm ./get_iplayer \
  && rm ./get_iplayer.cgi \
  && chmod 755 ./run.sh \
  && mkdir -p ${OUTPUT_DIR} \
  && chown ${USER_NAME}:${USER_NAME} ${OUTPUT_DIR} \
  && mkdir -p ${CONFIG_DIR} \
  && chown ${USER_NAME}:${USER_NAME} ${CONFIG_DIR} \
  && chown -R ${USER_NAME}:${USER_NAME} "/opt/get_iplayer"

USER ${USER_NAME}

EXPOSE 8181
VOLUME /config /downloads /archived
ENTRYPOINT [ "./run.sh" ]
