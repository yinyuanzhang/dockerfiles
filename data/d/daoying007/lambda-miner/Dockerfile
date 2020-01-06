FROM ubuntu:18.04
LABEL maintainer="daoying007 <daoying007@gmail.com>"
LABEL maintainer_eth_address="0xC53D71abA6C29F284836d76Df75a4967Cd96acf9"
LABEL maintainer_lambda_address="B68CBC296EC912D0C7E97EE0120086C13498C867"
LABEL github="https://github.com/daoying007/lambda-miner-docker"

RUN apt-get update
RUN apt-get install -y supervisor curl tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime

ARG MINER_VERSION="0.1.2"
ARG MINER_FILENAME="lambda_miner_${MINER_VERSION}.tar.gz"
ARG MINER_DIRNAME_ORIGIN="lambda_miner_${MINER_VERSION}"
ARG MINER_DIRNAME="lambda_miner"
ARG MINER_DOWNLOAD_URL="https://github.com/LambdaIM/TestNet/releases/download/v${MINER_VERSION}/${MINER_FILENAME}"

RUN cd /root/ \
    && curl -fSL ${MINER_DOWNLOAD_URL} -o ${MINER_FILENAME} \
    && tar xzf ${MINER_FILENAME} \
    && mv ${MINER_DIRNAME_ORIGIN} ${MINER_DIRNAME}

ADD etc/supervisor /etc/supervisor/
ADD scripts /root/
WORKDIR /root/lambda_miner

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]