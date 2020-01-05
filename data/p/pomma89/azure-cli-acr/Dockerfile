FROM docker:latest

LABEL description="Docker image with Azure CLI ready for ACR (Azure Container Registry) operations."
LABEL maintainer="Alessio Parma <alessio.parma@gmail.com>"

ENV PATH="${PATH}:/opt/azure-cli-acr/bin"

# Install Python 3 and PIP:
RUN apk add --update --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Install Azure CLI:
RUN apk add --update --no-cache bash && \
    apk add --update --no-cache --virtual=build gcc libffi-dev make musl-dev openssl-dev python3-dev && \
    pip install -U pip && \
    pip install azure-cli && \
    apk del --purge build && \
    rm -r /root/.cache

# Add custom scripts:
COPY bash /opt/azure-cli-acr/bin 
RUN find /opt/azure-cli-acr/bin -type f -print0 | xargs -0 chmod +x
