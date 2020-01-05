FROM ubuntu:14.04
MAINTAINER Etienne Batise <etienne.batise@gmail.com>

RUN apt-get update && \
    apt-get install -y python-pip && \
    pip install hyde && \
    useradd -ms /bin/bash mister && \
    passwd -d mister && \
    echo "mister ALL=(ALL:ALL) ALL" >> /etc/sudoers 

USER mister

WORKDIR /home/mister

EXPOSE 8080

ENTRYPOINT ["hyde"]

CMD ["serve","-a", "0.0.0.0", "-c", "site-production.yaml"]
