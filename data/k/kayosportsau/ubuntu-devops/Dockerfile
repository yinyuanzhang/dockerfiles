FROM kayosportsau/ubuntu-devops-base:1.0.20

ADD add /tmp

RUN mkdir /opt/sceptre-make && \
    cd /tmp/sceptre-make && \
    mv Makefile sceptre.mk /opt/sceptre-make && \
    mv sceptre-make.sh /usr/local/bin && \
    mv /tmp/customize/customize.sh /usr/local/bin
