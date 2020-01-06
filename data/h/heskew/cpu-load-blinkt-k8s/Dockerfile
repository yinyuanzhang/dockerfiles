FROM resin/rpi-raspbian:stretch

ENV WORKDIR=/usr/src/blinkt

RUN [ "cross-build-start" ]

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        python \
        python-rpi.gpio \
        python-psutil \
        gcc \
        python-pip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && mkdir -p "$WORKDIR"

# Cancel out any Entrypoint already set in the base image.
ENTRYPOINT []

WORKDIR "$WORKDIR"
COPY blinkt/library library

WORKDIR "$WORKDIR/library/"
RUN python setup.py install

WORKDIR "$WORKDIR"
COPY blinkt/examples cpu_load.py "$WORKDIR/examples/"
RUN pip install dumb-init

RUN [ "cross-build-end" ]

WORKDIR "$WORKDIR/examples/"

#ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/usr/src/blinkt/examples/cpu_load.py"]
CMD ["python", "/usr/src/blinkt/examples/cpu_load.py"]
