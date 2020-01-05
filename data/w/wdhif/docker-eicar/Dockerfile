FROM centos
LABEL maintainer "Wassim DHIF <wassimdhif@gmail.com>"

RUN yum install -y wget

RUN echo "Downloading EICAR file" && \
    wget --no-check-certificate https://www.eicar.org/download/eicar.com.txt

ENTRYPOINT sleep infinity

