FROM mcr.microsoft.com/dotnet/core/sdk:2.2.401-stretch

RUN apt-get update && \
    wget https://mcryptocdn.blob.core.windows.net/cos-internal/stuff/thrift_0.11.0-201901201852_amd64.deb && \
    dpkg -i thrift_0.11.0-201901201852_amd64.deb
