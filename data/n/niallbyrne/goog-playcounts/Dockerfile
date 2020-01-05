FROM alpine:3.8

ARG RUNTIME_USER=flask
ARG USER_UID=501

# Install the base system packages
RUN apk add --no-cache \
    bash \
    curl \
    gcc \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    musl-dev \
    openssl-dev \
    python3 \
    python3-dev

# Configure Python 3
RUN pip3 install -U pip && \
    pip3 install -U setuptools wheel && \
    ln -sf /usr/bin/python3 /usr/bin/python

# Create the runtime user to limit root inside the container
RUN addgroup ${RUNTIME_USER} && \
    adduser -u ${USER_UID} -G ${RUNTIME_USER} ${RUNTIME_USER} -D

# Project code will be installed to this subfolder
RUN mkdir -p /home/${RUNTIME_USER}/code && \
    mkdir -p /home/${RUNTIME_USER}/database
WORKDIR /home/${RUNTIME_USER}/code

# Install the Codebase and Python Packages
COPY requirements.txt /home/${RUNTIME_USER}/code
RUN pip3 install --no-cache-dir -Ur requirements.txt
COPY ./bin/entrypoint.sh /entrypoint.sh

# Enforce Permissions
COPY . /home/${RUNTIME_USER}/code
RUN chown -R ${RUNTIME_USER}:${RUNTIME_USER} /home/${RUNTIME_USER}
USER ${RUNTIME_USER}

EXPOSE 8000

# Entrypoint
CMD "/entrypoint.sh"
