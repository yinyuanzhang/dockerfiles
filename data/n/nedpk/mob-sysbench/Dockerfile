FROM centos:7

COPY ./sysbenchmdb /root/

RUN yum -y  install \
            mysql \
            mysql-devel\
            which \
            libtool \
            make \
            automake \
            numactl \
            sysstat\
            && yum clean all

RUN cd /root/sysbench-mariadb/ && ./autogen.sh && ./configure && make
RUN ln -s /root/mariadb-benchmarks/sysbench-runs/skeleton /sysbench-tests

ENTRYPOINT ["top", "-b"]

CMD ["-c"]