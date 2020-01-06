FROM oichuppa/base

ARG DEBIAN_FRONTEND="noninteractive"

ENV APP="XML_TV" CRON_TIME="30 1 * * *" XML_DAYS="7" XML_REGION="73"
VOLUME ["/data"]
VOLUME ["/logs"]

# install packages
RUN apt update
RUN apt upgrade -y
RUN apt install -y --no-install-recommends --no-install-suggests apt-utils git perl build-essential zlib1g-dev libcrypt-ssleay-perl openssl libssl-dev cron libclone-perl liburi-perl libfurl-perl libjson-perl libdatetime-perl libio-socket-ssl-perl libxml-writer-perl liblwp-protocol-https-perl libxml-simple-perl

# install XML_TV and Perl Modules
RUN git clone https://github.com/markcs/xml_tv.git ${APP_DIR}
        
# clean up
RUN apt purge -y build-essential
RUN apt autoremove -y
RUN apt clean
RUN rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /etc/cont-init.d/*

# move files around
COPY update-script.sh ${APP_DIR}/update-script.sh
RUN chmod +x ${APP_DIR}/update-script.sh
COPY yourtv.sh ${APP_DIR}/yourtv.sh
RUN chmod +x ${APP_DIR}/yourtv.sh
COPY root/ /