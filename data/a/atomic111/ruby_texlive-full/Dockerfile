# vim:set ft=dockerfile:

# for x86_64
FROM ubuntu:18.04

MAINTAINER Patrick Münch  <patrick.muench1111@gmail.com>

# Configure time zone and install ruby + texlive-full

RUN apt-get update \
    && apt-get install -y tzdata \
    && rm /etc/localtime \
    && ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get install -y ruby ruby-dev texlive-full gcc libffi-dev make zlib1g zlib1g-dev git locales nodejs npm python-pygments python3-pygments curl\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && locale-gen de_DE.UTF-8 \
    && update-locale LANG=de_DE.UTF-8

# Install MS Fonts and regenerate the font cache

RUN mkdir /usr/share/fonts/WindowsCalibriFont \
    && mkdir /usr/share/fonts/WindowsCambriaFont
COPY calibri_font_win10 /usr/share/fonts/WindowsCalibriFont
COPY cambria_font_win2016 /usr/share/fonts/WindowsCambriaFont
RUN chmod 755 /usr/share/fonts/WindowsCalibriFont/* \
    && chmod 755 /usr/share/fonts/WindowsCambriaFont/* \
    && fc-cache -f
