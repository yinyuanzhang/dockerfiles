FROM irremotus/zoneminder:latest

# Dependencies for building perl dependencies
RUN yum -y install sudo git gcc make
RUN yum -y install perl-CPAN perl-YAML-LibYAML perl-JSON

WORKDIR /root

# CPAN config
COPY cpan .cpan

# Perl dependencies
RUN perl -MCPAN -e "install Crypt::MySQL"
RUN perl -MCPAN -e "install Config::IniFiles"
RUN perl -MCPAN -e "install Net::WebSocket::Server"
RUN perl -MCPAN -e "install LWP::Protocol::https"
RUN perl -MCPAN -e "install Getopt::Long"

# Main repository
RUN git clone https://github.com/irremotus/zmeventnotification.git
WORKDIR zmeventnotification/

# Custom config
COPY zmeventnotification.ini .

# Dependencies for install script
RUN yum -y install which wget python-pip

# Install
ENV WEB_OWNER=apache WEB_GROUP=apache
RUN echo -e "\ny\ny\ny\ny\n" | ./install.sh
