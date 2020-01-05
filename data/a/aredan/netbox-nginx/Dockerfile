FROM lsiobase/nginx:3.10

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="aaNetworks build version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="Ariel Antigua"

# environment settings
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

# install packages
RUN \
 apk add --no-cache --upgrade \
	curl \
	git \
	nginx 
RUN cd /opt && pwd && git clone https://github.com/netbox-community/netbox.git && cd /opt/netbox/netbox/ && ls -la &&  cp -rf project-static /var/www/ && rm -rf netbox \
RUN cd /opt && rm -rf netbox
RUN cd /var/www/ && ls
RUN rm -f /etc/nginx/conf.d/default.conf

