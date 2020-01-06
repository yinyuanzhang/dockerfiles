FROM python:3.7.4-alpine3.10

RUN pip install pyyaml
RUN wget -q https://github.com/fluxcd/flux/releases/download/1.15.0/fluxctl_linux_amd64
RUN chmod +x fluxctl_linux_amd64
RUN mv fluxctl_linux_amd64 /usr/local/bin/fluxctl
COPY build.py /build.py
