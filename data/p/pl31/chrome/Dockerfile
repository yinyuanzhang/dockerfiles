FROM pl31/debian:stretch
MAINTAINER Patrick Büch <dh@paco.pl31.de>

# install services
RUN echo "Europe/Berlin" > /etc/timezone && \
    dpkg-reconfigure tzdata && \
    apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install \
        gdebi-core \
        pulseaudio && \
    curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    gdebi --option=APT::Get::force-yes=1,APT::Get::Assume-Yes=1 -n google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# run chrome
ENTRYPOINT ["google-chrome", "--no-sandbox", "--user-data-dir=/tmp/"]
