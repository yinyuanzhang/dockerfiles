FROM sagemathinc/cocalc
MAINTAINER Lorenzo "Palinuro" Faletra (palinuro@linux.it)
ENV DEBIAN_FRONTEND noninteractive
ENV VERSION 0.1

# Remove microsoft shit
RUN rm /etc/apt/sources.list.d/vscode.list; rm /etc/apt/trusted.gpg.d/microsoft.gpg /microsoft.gpg; apt-get -y remove code

# Add useful repos
RUN curl https://repository.vscodium.com/pub.gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/vscodium.gpg; \
    curl https://dbeaver.io/debs/dbeaver.gpg.key | gpg --dearmor > /etc/apt/trusted.gpg.d/dbeaver.gpg; \
    echo 'deb https://repository.vscodium.com/debs/ vscodium main' > /etc/apt/sources.list.d/vscodium.list; \
    echo "deb https://dbeaver.io/debs/dbeaver-ce /" > /etc/apt/sources.list.d/dbeaver.list

# Update everything
RUN apt-get update;apt-get -y install apt-transport-https; apt-get -y dist-upgrade ; rm -rf /var/lib/apt/lists/*

# Install additional software
RUN apt-get update; \
    apt-get -y install \
        codium dbeaver-ce avogadro emacs krita gimp \
        scilab geogebra sqlitebrowser mysql-workbench \
        gmysqlcc default-jdk nano

#Start CoCalc

CMD /root/run.py

EXPOSE 80 443
