FROM alpine:3.10

RUN apk add --no-cache python

RUN apk add --no-cache \
  build-base \
  sshpass

RUN apk add --no-cache \
    bash \
    py-pip \
    maven \
    openjdk8 \
    nodejs \
    npm


RUN apk add --no-cache \
    python3-dev \
    libffi-dev \
    openssl-dev \
    gcc \
    libc-dev \
    make

RUN apk add --no-cache python3 && \
    pip3 install --upgrade pip==19.3.1 setuptools==42.0.2 --no-cache

## Cleanup
RUN rm -rf /var/cache/apk/*

# Create a shared data volume
RUN mkdir /data/

## Expose some volumes
VOLUME ["/data"]
VOLUME ["/variables"]

ENV TEMPLATES_DIR /data
ENV VARS_DIR /variables

ENV SCRIPTS_DIR /home/dev/scripts
ENV OUT_DIR out
ENV TEMPLATE docker-compose.j2
ENV VARIABLES variables.yml
ENV WORKSPACE /tmp/

#app port
ENV PORT 8080

ENV TZ UTC

COPY ./ $SCRIPTS_DIR/
COPY ./inputs/templates/ $TEMPLATES_DIR/
COPY ./inputs/variables/ $VARS_DIR/

RUN chmod +x $SCRIPTS_DIR/*.py
RUN chmod +x $SCRIPTS_DIR/*.sh

WORKDIR /data

RUN pip3 install -r $SCRIPTS_DIR/requirements.txt

CMD ["python3", "/home/dev/scripts/main_flask.py"]
