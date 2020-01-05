FROM java:alpine
MAINTAINER Carlos Benevides<carlosbenevides@nasajon.com.br>
ENV SYM_VERSION "3.10"
ENV SYM_RELEASE "3.10.4"

RUN mkdir -p /opt
ADD https://sourceforge.net/projects/symmetricds/files/symmetricds/symmetricds-${SYM_VERSION}/symmetric-server-${SYM_RELEASE}.zip/download /opt/

RUN ls -la /opt && unzip /opt/download -d /opt/ \
    && mv /opt/symmetric-server-${SYM_RELEASE} /opt/symmetric/ \
    && rm -f /opt/download \
    && adduser -D symmetricds \
    && chown -R symmetricds /opt/symmetric \
    && chmod -R 775 /opt/symmetric

COPY reload_table.sh /opt/symmetric/bin/
COPY insertion_order.csv /opt/symmetric/bin/
COPY init.sh /opt/symmetric/

RUN chmod +x /opt/symmetric/bin/reload_table.sh
RUN chmod +x /opt/symmetric/init.sh

USER symmetricds

WORKDIR /opt/symmetric

ENTRYPOINT ["/opt/symmetric/init.sh"]
