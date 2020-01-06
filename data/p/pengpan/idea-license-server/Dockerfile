FROM alpine:latest
MAINTAINER MasterPan <i@hvv.me>

WORKDIR /root

ADD ./IntelliJIDEALicenseServer_linux_amd64 /root/IntelliJIDEALicenseServer_linux_amd64
ADD ./IntelliJIDEALicenseServer.html /root/IntelliJIDEALicenseServer.html

RUN chmod 777 ./IntelliJIDEALicenseServer_linux_amd64

EXPOSE 1027

#run license server
CMD ./IntelliJIDEALicenseServer_linux_amd64