FROM centos
RUN yum -y install unzip
ADD https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip 0.5.0_linux_amd64.zip
RUN unzip 0.5.0_linux_amd64.zip && mv consul /usr/bin/ && rm -f 0.5.0_linux_amd64.zip
VOLUME /data
EXPOSE 8400 8500 8600 8301 8302
ENTRYPOINT ["/usr/bin/consul"]
CMD ["agent", "-server", "-bootstrap-expect=1", "-client=0.0.0.0", "-data-dir=/data"]
