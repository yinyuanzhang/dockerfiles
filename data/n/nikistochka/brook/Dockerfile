FROM alpine:3.9
RUN mkdir -p /brookfolder
WORKDIR /brookfolder
RUN wget -O brook "https://github.com/txthinking/brook/releases/download/v20181212/brook" && chmod +x brook
ENTRYPOINT ["/brookfolder/brook"]
