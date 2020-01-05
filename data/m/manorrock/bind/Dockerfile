FROM manorrock/debian
ENV BIND_VERSION=1:9.11.5.P4+dfsg-5.1
RUN apt-get update && \ 
    apt-get install -y bind9=$BIND_VERSION && \
    rm -rf /var/lib/apt/lists/*
CMD ["/usr/sbin/named", "-g",  "-c", "/mnt/named.conf"]
