FROM alpine:3.8

RUN apk --no-cache update && \
    apk --no-cache upgrade
    
RUN apk --no-cache add \
      bash \
      bash-completion \
      groff \
      less \
      curl \
      jq \
      python3 \
      git \
      openssh && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install --upgrade \
      awscli && \
    ln -s /usr/bin/aws_bash_completer /etc/profile.d/aws_bash_completer.sh &&\
    rm -rf /tmp/* && \
    mkdir ~/.aws && \
    chmod 700 ~/.aws && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Expose volume for adding credentials
VOLUME ["~/.aws"]

CMD ["/bin/bash"] 
