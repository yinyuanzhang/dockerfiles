FROM ubuntu:16.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget csh

WORKDIR /opt
RUN wget --no-check-certificate --http-user=download --http-password=mpm3fd \
    http://cns-online.org/download/v1.3/cns_solve_1.3_all_intel-mac_linux.tar.gz
RUN tar -xzf cns_solve_1.3_all_intel-mac_linux.tar.gz

WORKDIR /opt/cns_solve_1.3
RUN sed -i "s%_CNSsolve_location_%/opt/cns_solve_1.3%g" .cns_solve_env_sh
RUN sed -i "s%_CNSsolve_location_%/opt/cns_solve_1.3%g" cns_solve_env

COPY wrapper.sh /opt/cns_solve_1.3

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/cns_solve_1.3/wrapper.sh"]
