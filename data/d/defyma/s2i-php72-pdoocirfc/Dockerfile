FROM defyma/s2i-php72-pdooci:v1.0.2

USER root

RUN yum install -y centos-release-scl && \
    INSTALL_PKGS="rh-php72-php-devel compat-libstdc++-33" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y



#RUN mkdir /opt/app-root/sap
RUN mkdir -p /usr/sap/nwrfcsdk
RUN mkdir /opt/app-root/saprfc

COPY ./nwrfcsdk /usr/sap/nwrfcsdk

#ADD ./rfcsdk.tar.gz /usr/sap
#ADD ./saprfc-1.4.1.tar.gz /opt/app-root
#COPY ./saprfc-1.4.1 /opt/app-root/saprfc

RUN echo “/usr/sap/nwrfcsdk/lib” > /etc/ld.so.conf.d/nwrfcsdk.conf; \
	ldconfig


RUN cd /opt/app-root/saprfc; \
	git clone https://github.com/defyma/php7-sapnwrfc.git; \
	cd php7-sapnwrfc; \
	phpize; \
	./configure --with-sapnwrfc=/usr/sap/nwrfcsdk/; \
	make install

#RUN cd /opt/app-root/saprfc && \
# phpize && \
# ./configure --with-sap=/usr/sap/rfcsdk/ && \
# make && \
# make install && \
# make clean

RUN echo "extension=sapnwrfc" > /etc/opt/rh/rh-php72/php.d/99-sapnwrfc.ini

USER 1001

# Set the default CMD to print the usage of the language image
CMD $STI_SCRIPTS_PATH/usage
