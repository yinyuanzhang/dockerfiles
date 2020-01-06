FROM alpine:3.9
LABEL maintainer="cidr32"
WORKDIR /root

ENV PATH ~/.local/bin:$PATH
ENV LC_ALL=en_US.UTF-8
ENV ENV="/etc/profile"
#ENV ENV="/root/.ashrc"

RUN apk upgrade --no-cache && \
    apk add --no-cache bash bash-completion bash-doc nano grep curl shadow bind-tools busybox-extras \
    python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install awscli --upgrade --user && \
    pip3 install boto3 --upgrade --user && \
    pip3 install boto --upgrade --user && \
    sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd && \
    rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

SHELL ["/bin/bash", "-c"]

RUN echo -e "complete -C '/root/.local/bin/aws_completer' aws\nPS1=\"[ \u@awscli \W]\\$ \"\nTERM=screen-256color" >> /root/.bashrc && \
    echo -e "complete -C '/root/.local/bin/aws_completer' aws" >> /etc/profile && \
    cp /etc/profile /root/.profile && \
    . /etc/profile

CMD ["/bin/bash"]
