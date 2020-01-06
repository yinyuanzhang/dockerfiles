FROM mcr.microsoft.com/dotnet/core/aspnet:3.0.0-disco

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y locales && \ 
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    update-locale LANG=en_US.UTF-8

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    DSE_CONTAINER_BASE=ASPNET_RUNTIME \
    DSE_CONTAINER_BASE_VERSION=3.0.0-rc1 \
    DSE_CONTAINER_VERSION=3.0.0-rc1-3