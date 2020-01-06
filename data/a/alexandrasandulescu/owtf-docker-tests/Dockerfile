FROM kalilinux/kali-linux-docker

MAINTAINER @delta24 viyat001@gmail.com, @alexandrasandulescu alecsandra.sandulescu@gmail.com

RUN apt-get update && apt-get upgrade -y

# install required packages from Kali repos
COPY packages.sh /
RUN ["sh", "packages.sh"]

# upgrade pip and install required python packages
COPY owtf.pip /
RUN ["pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "--upgrade", "-r", "owtf.pip"]

#Kali SSL lib-fix
ENV PYCURL_SSL_LIBRARY openssl

RUN apt-get update --fix-missing
COPY optional_tools.sh /usr/bin/
RUN chmod +x /usr/bin/optional_tools.sh


RUN /bin/bash /usr/bin/optional_tools.sh

#download latest OWTF
RUN git clone -b fix_msfcli https://github.com/alexandrasandulescu/owtf.git
RUN mkdir owtf/tools/restricted
# allow access to the web ui from outside
COPY framework_config.cfg.patch owtf/

# core installation
RUN python owtf/install/install.py --no-user-input --core-only

# DB installation and setup
COPY postgres_entry.sh owtf/scripts/
RUN chmod +x owtf/scripts/postgres_entry.sh

# expose ports
EXPOSE 8010 8009 8008

# cleanup
RUN rm packages.sh owtf.pip

#COPY optional_tools.sh /usr/bin/
#RUN chmod +x /usr/bin/optional_tools.sh

#setup postgres
USER postgres
ENV PG_MAJOR 9.1
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# setting user to root
ENV USER root
USER root

#set entrypoint
COPY owtf_entry.sh /usr/bin/
RUN chmod +x /usr/bin/owtf_entry.sh

ENTRYPOINT ["/usr/bin/owtf_entry.sh"]
