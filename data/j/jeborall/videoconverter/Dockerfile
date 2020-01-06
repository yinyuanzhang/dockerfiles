FROM alpine:3.10

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

# Install Python
RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

# Install ffmpeg dependency
RUN apk add ffmpeg

# Install dev-build requirements
RUN apk add build-base python3-dev libffi-dev libressl-dev linux-headers libc-dev musl
ADD * /

# Install pip requirement modules
RUN pip install python-ffmpeg-video-streaming

CMD [ "python", "./convert.py" ]