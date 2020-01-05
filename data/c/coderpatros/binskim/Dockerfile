FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS builder

RUN cd /tmp && \
    git clone --depth 1 https://github.com/microsoft/binskim.git && \
    mkdir /tmp/binary && \
    dotnet publish --configuration Release --framework netcoreapp2.0 --runtime linux-x64 --output /tmp/binary /tmp/binskim/src/BinSkim.Driver/BinSkim.Driver.csproj && \
    chmod +x /tmp/binary/BinSkim


FROM ubuntu:18.04

COPY --from=builder /tmp/binary /usr/share/binskim

RUN ln -s /usr/share/binskim/BinSkim /usr/bin/binskim && \
    apt-get update && \
    apt-get install -y icu-devtools libunwind8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


ENTRYPOINT [ "binskim" ]
CMD [ "binskim" ]