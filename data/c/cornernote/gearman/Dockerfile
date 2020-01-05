FROM debian
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update; \
    apt-get upgrade

RUN apt-get --yes --force-yes install gearman-job-server gearman mod-gearman-tools; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*

EXPOSE 4730
ENTRYPOINT [ "gearmand" ]
