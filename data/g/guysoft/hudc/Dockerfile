FROM php:5.3-apache
MAINTAINER Guy Sheffer <guysoft@gmail.com>
EXPOSE 22

ENV LANG_WHICH en
ENV LANG_WHERE US
ENV ENCODING UTF-8
ENV LANGUAGE ${LANG_WHICH}_${LANG_WHERE}.${ENCODING}
ENV LANG ${LANGUAGE}

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    tzdata \
    apt-utils \
    wget \
    locales \
    sudo \
    unzip \
  && locale-gen ${LANGUAGE} \
  && locale-gen he_IL.UTF-8 \
  && dpkg-reconfigure --frontend noninteractive locales \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get -qyy clean

#===================
# Timezone settings
#===================
# Full list at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
#  e.g. "US/Pacific" for Los Angeles, California, USA
# e.g. ENV TZ "US/Pacific"
ENV TZ="Asia/Jerusalem"
# Apply TimeZone
# Layer size: tiny: 1.339 MB
RUN echo "Setting time zone to '${TZ}'" \
  && echo "${TZ}" > /etc/timezone \
  && dpkg-reconfigure --frontend noninteractive tzdata

