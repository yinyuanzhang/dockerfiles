FROM saearagon/ubuntuvncserver
MAINTAINER Servicio de Administracion Electrónica
RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install firefox chromium-browser

COPY runcontainer_vncbrowsers /usr/bin/runcontainer_vncbrowsers
RUN chmod 777 -R /usr/bin/runcontainer_vncbrowsers
COPY containervncbrowsers-setup.sh /usr/bin/containervncbrowsers-setup.sh
RUN chmod 777 -R /usr/bin/containervncbrowsers-setup.sh

ENTRYPOINT ["/bin/bash", "-c", "/usr/bin/runcontainer_vncbrowsers"]
