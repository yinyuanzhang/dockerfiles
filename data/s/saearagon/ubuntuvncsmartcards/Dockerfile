FROM saearagon/ubuntuvncbrowsers
MAINTAINER Servicio de Administracion Electrónica
RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install pcscd pcsc-tools screen p11-kit libnss3 libnss3-tools libccid opensc pinentry-gtk2 bash supervisor

WORKDIR "/tmp"
RUN wget https://www.sede.fnmt.gob.es/documents/10445900/10700711/libpkcs11-fnmtdnie_1.5.0_Ubuntu_18.04_LTS_18.10_64bits.deb
RUN dpkg -i libpkcs11-fnmtdnie_1.5.0_Ubuntu_18.04_LTS_18.10_64bits.deb
RUN wget http://cdn.bit4id.com/es/soporte/downloads/middleware/Bit4id_Middleware.zip
RUN unzip Bit4id_Middleware.zip
RUN cp "Linux_ 4.0.0.5/linux64/libbit4ipki.so" /usr/lib/libbit4ipki.so
RUN cp "Linux_ 4.0.0.5/linux64/libbit4ipki.so" /usr/local/lib/libbit4ipki.so
RUN cp -r "Linux_ 4.0.0.5/linux64/pinman_64_bit" /usr/local/lib/pinman_64_bit
COPY configUserNssdb /usr/bin/configUserNssdb
RUN chmod 777 -R /usr/bin/configUserNssdb
COPY runcontainer_vncsmartcard /usr/bin/runcontainer_vncsmartcard
RUN chmod 777 -R /usr/bin/runcontainer_vncsmartcard
COPY containervncsmartcard-setup.sh /usr/bin/containervncsmartcard-setup.sh
RUN chmod 777 -R /usr/bin/containervncsmartcard-setup.sh
COPY supervisord.conf /etc/supervisord.conf
#RUN ls -lisa /usr/bin/config*
RUN mkdir /run/sshd
ENTRYPOINT ["/bin/bash", "-c", "/usr/bin/runcontainer_vncsmartcard"]