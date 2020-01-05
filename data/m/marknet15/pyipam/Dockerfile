FROM alpine:3.8

LABEL maintainer="Mark Woolley <mw@marknet15.com>"
LABEL version="0.1.4"
LABEL description="PyIPAM Docker Container"

# Required Vars
ENV PYIPAM_VERSION v0.1.4

# Install required package
RUN apk add --update --no-cache python3 python3-dev git gcc musl-dev postgresql-libs postgresql-dev && \
    pip3 install --upgrade pip

# General setup
RUN git clone https://github.com/marknet15/pyipam.git --branch "${PYIPAM_VERSION}" && \
    pip3 install pyipam/ && \
    rm -R pyipam && \
    ln -s /usr/lib/python3.6/site-packages/pyipam/config /config

# Expose port to be published
EXPOSE 5000

# Create exposed volume
VOLUME ["/config"]

# Add entrypoint
ADD entrypoint.sh /
RUN chmod a+x entrypoint.sh

# Run Pypi server
CMD ["/entrypoint.sh"]