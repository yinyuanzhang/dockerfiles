FROM ubuntu:16.04
LABEL maintainer="Emilio González Montaña <emilio@ociotec.com>"

RUN apt-get update && \
    apt-get install -y sysbench && \
    rm -rf /var/lib/apt/lists/*

CMD while true; do sysbench --test=cpu --batch --batch-delay=5 --cpu-max-prime=100000 --num-threads=1 run; done

