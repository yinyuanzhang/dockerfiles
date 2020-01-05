FROM alpine
RUN apk update
RUN apk add bash
RUN apk add openssh
RUN apk add git
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache && \
    pip3 install requests
RUN apk add openjdk8
RUN apk add apache-ant --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
    --allow-untrusted
ENV ANT_HOME /usr/share/java/apache-ant
ENV PATH $PATH:$ANT_HOME/bin