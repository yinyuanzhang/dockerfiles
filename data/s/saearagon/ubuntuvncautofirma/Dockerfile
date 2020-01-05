FROM saearagon/ubuntuvncsmartcards
MAINTAINER Servicio de Administracion Electrónica
ENV DEBIAN_FRONTEND=noninteractive

COPY certs/ /tmp/certs/
COPY firefox/ /tmp/firefox

RUN apt-get update
RUN apt-get install -y openjdk-8-jre gkrellm dos2unix

WORKDIR "/tmp"
RUN wget https://estaticos.redsara.es/comunes/autofirma/currentversion/AutoFirma_Linux.zip
RUN unzip AutoFirma_Linux.zip
RUN dpkg -i AutoFirma_1_6_5.deb

COPY runcontainer_vncautofirma /usr/bin/runcontainer_vncautofirma
RUN chmod 777 -R /usr/bin/runcontainer_vncautofirma
COPY containervncautofirma-setup.sh /usr/bin/containervncautofirma-setup.sh
RUN chmod 777 -R /usr/bin/containervncautofirma-setup.sh

ENTRYPOINT ["/bin/bash", "-c", "/usr/bin/runcontainer_vncautofirma"]