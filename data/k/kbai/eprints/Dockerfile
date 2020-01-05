# http://files.eprints.org/1101/1/eprints-3.4-preview-2.tgz
# EPrints 3.4 has the same prerequisites as 3.3.
# We advise installing eprints into /opt, and running apache as the eprints user

# As the root user download both eprints-3.4-preview-2.tgz and eprints_publication_flavour-3.4-preview-2.tgz and put them into /root/
# Then also as root install the files:

# cd /opt
# tar xzf ~/eprints-3.4-preview-2.tgz
# cd /opt/eprints3
# tar xzf ~/eprints_publication_flavour-3.4-preview-2.tgz
# chown -R eprints:eprints /opt/eprints3

# # change to the eprints user
# su - eprints
# cd /opt/eprints3

# # to create a minimal repository
# bin/epadmin create zero

# # or to create a publications repository
# bin/epadmin create publication
FROM ubuntu:16.04
WORKDIR /opt/eprints3

# ENV EPRINTS_TARBALL_URL="http://files.eprints.org/1101/1/eprints-3.4-preview-2.tgz"
ENV EPRINTS_TARBALL="eprints-3.4-preview-2.tgz"
ENV EPRINTS_TARBALL_PUBL="eprints_publication_flavour-3.4-preview-2.tgz"
ENV DEBIAN_FRONTEND=noninteractive

# Dependencies taken from the Debian source package control file:
# lynx \
# libselinux1 \
# libsepol1 \
RUN apt-get update -y && apt-get install -y \
    perl \
    libncurses5 \
    apache2 \
    libapache2-mod-perl2 \
    libxml-libxml-perl \
    libunicode-string-perl \
    libterm-readkey-perl \
    libmime-lite-perl \
    libmime-types-perl \
    libxml-libxslt-perl \
    libdigest-sha-perl \
    libxml-parser-perl \
    libxml2-dev \
    libxml-twig-perl \
    libarchive-any-perl \
    libjson-perl \
    libsearch-xapian-perl \
    libcgi-pm-perl \
    libdbi-perl \
    libdbd-mysql-perl \
    elinks \
    wget \
    ghostscript \
    xpdf \
    antiword \
    pdftk \
    texlive-base \
    texlive-base-bin \
    psutils \
    imagemagick \
    adduser \
    unzip

# Dependencies taken from the Debian source package control file:
RUN apt-get update -y && apt-get install -y sudo expect 

ADD eprints-3.4-preview-2.tgz /opt
ADD eprints_publication_flavour-3.4-preview-2.tgz /opt/eprints3
ADD install.expect install.expect
ADD install.sh install.sh

RUN useradd eprints
RUN chown -R eprints:eprints /opt/eprints3
# RUN bash install.sh

EXPOSE 80
CMD sudo service apache2 stop && /usr/sbin/apache2ctl -D FOREGROUND
