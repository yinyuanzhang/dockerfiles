# Requires docker 17.05

# Run sample docker run --restart unless-stopped -d --name moxd -p 38081:38081 --mount type=bind,source=/media/data01/moxdata,target=/moxdata quickminer/mox
#FROM ubuntu:16.04
FROM ubuntu:17.10
#FROM ubuntu:18.04

RUN apt-get update && \
    apt-get --no-install-recommends --yes install \
    language-pack-en-base \
    ca-certificates \
    unzip \
    pcscd \
    wget && \
    export LC_ALL=en_US.UTF-8 && \
    export LANG=en_US.UTF-8

# blockchain volume data
VOLUME /moxdata

## download && extrack & chmod
RUN wget https://github.com/mox-project/MoX/releases/download/v1.1.0/ubuntu17-x64-1.0.0.zip -P /moxd/ && \
    unzip /moxd/ubuntu17-x64-1.0.0.zip -d /moxd && \
    chmod +x /moxd/ubuntu17-x64-1.0.0/moxd


# Generate your wallet via accessing the container and run:
# docker exec -it moxd /bin/bash
# cd /moxd/ubuntu17-x64-1.0.0.zip
# ./mox-wallet-cli --daemon-address=127.0.0.1:38081


EXPOSE 38080
EXPOSE 38081
ENTRYPOINT ["/moxd/ubuntu17-x64-1.0.0/moxd", "--p2p-bind-ip=0.0.0.0", "--p2p-bind-port=38080", "--rpc-bind-ip=0.0.0.0", "--rpc-bind-port=38081", "--non-interactive", "--confirm-external-bind", "--data-dir=/moxdata/.mox"] 

