FROM mcr.microsoft.com/dotnet/core/runtime:2.1-stretch-slim

LABEL maintainer "Yefta Sutanto <yefta@bitwyre.com>"

COPY . /app/bitwyre/fixbridge
WORKDIR /app/bitwyre/fixbridge
RUN chmod +x ./setup.sh; chmod +x ./run.sh

EXPOSE 5001 9092

ENTRYPOINT ./run.sh
