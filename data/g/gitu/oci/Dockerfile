FROM gitu/oci:19


RUN  yum -y group install "Development Tools" && \
     yum -y install oracle-golang-release-el7 && yum -y install golang && \
     rm -rf /var/cache/yum

CMD ["sqlplus", "-v"]
