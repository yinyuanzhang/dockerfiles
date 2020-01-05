FROM debian:latest
MAINTAINER clemensvb <cjvb@gmx.net>
#forked from MAINTAINER firsttris <info@teufel-it.de>

# master, unstable, testing, stable
ENV tvh_release=stable

ENV _clean="rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*"
ENV _apt_clean="eval apt-get clean && $_clean"

ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update -qq \
 && apt-get install -qqy apt-transport-https software-properties-common bzip2 libavahi-client3 libav-tools xmltv wget udev gnupg2 socat

# Add key and tvheadend repository
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61
#RUN apt-add-repository "https://dl.bintray.com/tvheadend/deb ${tvh_release}"

RUN wget https://doozer.io/keys/tvheadend/tvheadend/pgp
RUN apt-key add pgp
RUN sh -c 'echo "deb https://apt.tvheadend.org/${tvh_release} $(lsb_release -sc) main" | tee -a /etc/apt/sources.list.d/tvheadend.list'


# Install tvheadend non interactive
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq \
 && apt-get install -qqy tvheadend

# Install Sundtek DVB Driver
RUN wget http://www.sundtek.de/media/sundtek_netinst.sh \
 && chmod 777 sundtek_netinst.sh \
 && ./sundtek_netinst.sh -easyvdr

# Add Basic config
ADD config /config/

# Timezone
RUN echo "Europe/Berlin" > /etc/timezone

# Create Locales
ENV LANG="de_DE.UTF-8"
RUN apt-get update -qqy && apt-get install -qqy locales && $_apt_clean \
 && grep "$LANG" /usr/share/i18n/SUPPORTED >> /etc/locale.gen && locale-gen \
 && update-locale LANG=$LANG

# Configure the hts user account and it's folders
RUN groupmod -o -g 9981 hts \
 && usermod -o -u 9981 -a -G video -d /config hts \
 && install -o hts -g hts -d /config /recordings

# Launch script
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Default container settings
VOLUME /config /recordings /picons
EXPOSE 9981 9982
ENTRYPOINT ["/entrypoint.sh"]
