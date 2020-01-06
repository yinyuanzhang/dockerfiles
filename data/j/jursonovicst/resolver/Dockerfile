FROM alpine

#Create #cpus worker threads to take advantage of multiple CPUs. If not specified, named will try to determine the number of CPUs present and create one thread per CPU. If it is unable to determine the number of CPUs, a single worker thread will be created.
ENV NAMED_CPUS=2

RUN apk --no-cache add bind
EXPOSE 53 53/udp
COPY named.conf /etc/bind/
ENTRYPOINT /usr/sbin/named -c /etc/bind/named.conf -g -u named -n ${NAMED_CPUS}

