FROM centos:7
LABEL maintainer "Jian Zeng <anonymousknight96@gmail.com>"
EXPOSE 5201
ENTRYPOINT ["iperf3"]
CMD ["-s"]
ADD ["aliyun-epel-7.repo", "aliyun-centos-base-7.repo", "/"]
RUN yum install -y epel-release && \
    yum install -y telnet tcpdump nc iperf3 httpd-tools qperf net-tools bind-utils less iproute bmon sockperf vim jq git siege stress-ng sysbench && \
    yum clean all && rm -rf /var/cache/yum
