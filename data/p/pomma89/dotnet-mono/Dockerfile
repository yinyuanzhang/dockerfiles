FROM pomma89/dotnet:3-sdk

LABEL description="Docker images with .NET Core and Mono, based on Debian Linux."
LABEL maintainer="Alessio Parma <alessio.parma@gmail.com>"

ENV MONO_VERSION="6.6"

COPY ./bash bash
RUN sh bash/common.setup.sh &&\
    sh bash/sdk.mono.sh &&\
    sh bash/common.cleanup.sh &&\
    rm -rf bash
