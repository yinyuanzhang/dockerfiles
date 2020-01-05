FROM python:3.7

RUN useradd -d /opt/powerapi -m powerapi
WORKDIR /opt/powerapi
USER powerapi

RUN pip3 install --user numpy

ENTRYPOINT ["/bin/echo", "0.4"]
