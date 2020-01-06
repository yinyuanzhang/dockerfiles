FROM buildpack-deps:stretch-curl as downloader

ARG FIREFOX_VERSION=70.0

ARG FIREFOX_LANGUAGE=en-US

ADD https://archive.mozilla.org/pub/firefox/releases/${FIREFOX_VERSION}/KEY KEY

RUN gpg --no-tty --import KEY

ADD https://archive.mozilla.org/pub/firefox/releases/${FIREFOX_VERSION}/SHA512SUMS SHA512SUMS

ADD https://archive.mozilla.org/pub/firefox/releases/${FIREFOX_VERSION}/SHA512SUMS.asc SHA512SUMS.asc

RUN gpg --verify SHA512SUMS.asc

# need RUN rather than ADD or COPY because both ADD and COPY are silently unzipping the archive
RUN wget --no-verbose --show-progress --progress=dot:giga --directory-prefix linux-x86_64/${FIREFOX_LANGUAGE} https://archive.mozilla.org/pub/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/${FIREFOX_LANGUAGE}/firefox-${FIREFOX_VERSION}.tar.bz2

RUN grep linux-x86_64/${FIREFOX_LANGUAGE}/firefox-${FIREFOX_VERSION}.tar.bz2 SHA512SUMS | sha512sum -c -

RUN apt-get --quiet update && DEBIAN_FRONTEND=noninteractive apt-get --quiet --assume-yes install bzip2

RUN tar --extract --bzip2 --file linux-x86_64/${FIREFOX_LANGUAGE}/firefox-${FIREFOX_VERSION}.tar.bz2 --directory tmp/


FROM ubuntu:18.04 as firefox

COPY --from=downloader /tmp/firefox /usr/lib/firefox

RUN apt-get --quiet update && DEBIAN_FRONTEND=noninteractive apt-get --quiet --assume-yes install evince libgtk-3-0 libdbus-glib-1-2 libxt6 libcanberra-gtk-module libcanberra-gtk3-module tzdata libx11-xcb1

RUN apt-get --quiet update && DEBIAN_FRONTEND=noninteractive apt-get --quiet --assume-yes install flashplugin-installer browser-plugin-freshplayer-pepperflash

RUN mkdir --parents /usr/lib/firefox/plugins

RUN cp /usr/lib/flashplugin-installer/libflashplayer.so /usr/lib/firefox/plugins/libflashplayer.so

RUN cp /usr/lib/flashplugin-installer/libflashplayer.so /usr/lib/mozilla/plugins/libflashplayer.so

RUN [ "/usr/lib/firefox/firefox", "-headless", "-CreateProfile", "custom /root/.mozilla/firefox/custom" ]

ENTRYPOINT [ "/usr/lib/firefox/firefox" ]
