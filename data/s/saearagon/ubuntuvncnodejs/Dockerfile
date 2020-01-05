FROM saearagon/ubuntuvncautofirma
MAINTAINER Servicio de Administracion Electrónica
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y nodejs npm zenity xdotool libaio1 expect
WORKDIR "/tmp"
RUN wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chmod 777 /usr/bin/chromedriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
RUN tar xzvf geckodriver-v0.24.0-linux64.tar.gz
RUN mv geckodriver /usr/bin/geckodriver
RUN chmod 777 /usr/bin/chromedriver

COPY runcontainer_vncnodejs /usr/bin/runcontainer_vncnodejs
RUN chmod 777 -R /usr/bin/runcontainer_vncnodejs
COPY containervncnodejs-setup.sh /usr/bin/containervncnodejs-setup.sh
RUN chmod 777 -R /usr/bin/containervncnodejs-setup.sh

RUN mkdir -p /usr/src/app
COPY nodejsExpressHelloWorld.js /usr/src/app/main.js
RUN chmod 777 -R /usr/src/app/main.js

COPY instantclient_12_1.zip ./
RUN unzip instantclient_12_1.zip && \
    mv instantclient_12_1/ /usr/lib/ && \
    rm instantclient_12_1.zip && \
    ln /usr/lib/instantclient_12_1/libclntsh.so.12.1 /usr/lib/libclntsh.so && \
    ln /usr/lib/instantclient_12_1/libocci.so.12.1 /usr/lib/libocci.so && \
    ln /usr/lib/instantclient_12_1/libociei.so /usr/lib/libociei.so && \
    ln /usr/lib/instantclient_12_1/libnnz12.so /usr/lib/libnnz12.so

ENV ORACLE_BASE /usr/lib/instantclient_12_1
ENV LD_LIBRARY_PATH /usr/lib/instantclient_12_1
ENV TNS_ADMIN /usr/lib/instantclient_12_1
ENV ORACLE_HOME /usr/lib/instantclient_12_1

RUN ldconfig

WORKDIR "/usr/src/app"
RUN npm install express

ENTRYPOINT ["/bin/bash", "-c", "/usr/bin/runcontainer_vncnodejs"]