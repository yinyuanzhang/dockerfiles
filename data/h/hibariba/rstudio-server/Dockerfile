############################################################
# Dockerfile to build Rstudio server
# Based on CentOS
############################################################

FROM centos:6.6
MAINTAINER hibariba

################## BEGIN INSTALLATION ######################

# add EPEL
RUN yum install -y epel-release

# install R
RUN yum install -y R-3.1.2
# config java for R
RUN R CMD javareconf -e

# install rstudio server dependencies
RUN yum install -y \
    libcrypto.so.6 \
    libgfortran.so.1 \
    libssl.so.6 \
    openssl098e-0.9.8e \
    pango-1.28.1 \
    wget
RUN wget --no-verbose  ftp.scientificlinux.org/linux/scientific/6.0/x86_64/os/Packages/compat-libgfortran-41-4.1.2-39.el6.x86_64.rpm
RUN rpm -Uvh compat-libgfortran-41-4.1.2-39.el6.x86_64.rpm

# install rstudio server
RUN wget --no-verbose http://download2.rstudio.org/rstudio-server-0.97.336-x86_64.rpm
RUN rpm -Uvh --nodeps rstudio-server-0.97.336-x86_64.rpm

# ##################### INSTALLATION END #####################

# add example user
# RUN groupadd r_users
# RUN useradd -G r_users ruser1
# RUN (echo "john:123" | chpasswd)
COPY userconf.sh /usr/bin/userconf.sh

# add supervisor
RUN yum install -y supervisor
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /etc/supervisor/conf.d
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf


EXPOSE 8787

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]