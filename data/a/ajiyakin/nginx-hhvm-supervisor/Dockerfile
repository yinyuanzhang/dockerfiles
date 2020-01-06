FROM ubuntu:trusty
MAINTAINER Aji Yakin<ajiyakin91@gmail.com>

# Preconfigure
RUN apt-get install -qq -y software-properties-common

# Add HHVM repository
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449
RUN add-apt-repository -y "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"

# Update
RUN apt-get update -qq -y

# Install HHVM and Supervisor
RUN apt-get install -qq -y nginx hhvm supervisor

# Clean and remove unnecesary package to make image small
RUN apt-get autoremove -qq -y && \
    apt-get autoclean -qq -y


# ----------------------------------------------------------------------------
# Configurations

# Install fastcgi for HHVM
RUN /usr/share/hhvm/install_fastcgi.sh

# Turn off nginx daemon
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Add all files under supervisor.conf.d/* to /etc/supervisor/conf.d/
ADD ./resources/supervisor/conf.d/* /etc/supervisor/conf.d/

# Add and prepare starter file
ADD ./resources/start.sh /start.sh
RUN chmod 775 /start.sh

# Private expose
EXPOSE 80


# ----------------------------------------------------------------------------
# Start all services on foreground via supervisor

CMD /bin/bash /start.sh

