FROM       alpine
MAINTAINER Mauricio Araya

ENV LANGUAGE=en_US
ENV LANG=en_US.UTF-8
ENV JEKYLL_VERSION=3.5.1
ENV JEKYLL_ENV=production
ENV LC_ALL=en_US

RUN apk update
RUN apk add --update zlib-dev \
                     build-base \
                     libxml2-dev \
                     libxslt-dev \
                     readline-dev \
                     libffi-dev \
                     yaml-dev \
                     zlib-dev \
                     libffi-dev

RUN apk add --update zlib \
                     libxml2 \
                     readline \
                     libxslt \
                     ruby yaml \
                     libffi \
                     git \
                     openssl \
                     tzdata \
                     bash \
                     jq \
                     wget \
                     unzip \
                     ncurses \
                     shadow \
                     curl


RUN apk add --no-cache python3 python3-dev && \
    pip3 install --upgrade pip setuptools && \
    pip3 install --upgrade awscli hovercraft && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

RUN mkdir -p /usr/local/share && \
    wget "https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh" -O /usr/local/share/git-prompt.sh -o /dev/null

RUN adduser -h /home/hovercraft -s /bin/bash hovercraft -D && \
    mkdir -p /home/hovercraft/.ssh \
             /home/hovercraft/workdir \
             /home/hovercraft/bin \
             /home/hovercraft/tmp

COPY bashrc /home/hovercraft/.bashrc
COPY curlrc /home/hovercraft/.curlrc
COPY inputrc /etc/inputrc
COPY presentation /home/hovercraft/bin

RUN chmod 644 /etc/inputrc

RUN chown -R hovercraft:hovercraft /home/hovercraft && \
    chmod -R og-rwx /home/hovercraft && \
    chmod 700 /home/hovercraft/bin/presentation

WORKDIR /home/hovercraft/workdir

ENTRYPOINT ["/bin/bash"]
