FROM ibmjava:8-sdk
MAINTAINER Ramso code@ramso.net
LABEL description="Contanedor para usar soap ui. \
Soporta dos mandatos [test|mockup], por defecto test \
-test lanza testrunner de un proyecto \
-mockup lanza mockservicerunner de un proyecto \
Se puede usar un volumen en /var/soapui donde pondremos los proyectos y donde se almacenaran los resultados. \
Hay varias variables de entorno para ajustar el uso del contenedor: \
-PROJECT el nombre del fichero con el proyecto de soapui. Es obligatorio\
-PORT el numero de puerto para los mockups. Opcional si no se usara el 8088.\
-SUITE el nombre del testsuite o del mockup a levantar. Opcional si no se indica se realizara para todo el proyecto.\
-OPTIONS Cualquier otro opcion en linea de mandatos que queramos usar para ejecutar el proyecto. Opcional"

# Install curl
RUN export DEBIAN_FRONTEND=noninteractive && \
    export LC_ALL=en_US.UTF-8 && \
    apt-get update && \
    apt-get install -y curl gosu

# SOAP UI Version to download

ARG SOAPUI_VERSION
ENV SOAPUI_VERSION ${SOAPUI_VERSION:-5.4.0}


ENV PORT 8088

EXPOSE ${PORT}

# Download and unarchive SoapUI
RUN mkdir -p /opt &&\
    curl  https://s3.amazonaws.com/downloads.eviware/soapuios/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-bin.tar.gz \
    | gunzip -c - | tar -xf - -C /opt && \
    ln -s /opt/SoapUI-${SOAPUI_VERSION} /opt/SoapUI

# Create user path
ENV PROJECT_PATH /var/soapui

RUN mkdir -p ${PROJECT_PATH}

VOLUME ${PROJECT_PATH}


# Set environment
ENV PATH ${PATH}:/opt/SoapUI/bin

ENV PROJECT null

ENV OPTIONS ''

COPY docker-entrypoint.sh /usr/local/bin/
run chmod a+x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]

WORKDIR /opt/SoapUI/bin

CMD ["test"]
