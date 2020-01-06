FROM ibandrea/mariadb:10.0.28
MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>

# Let mariadb run as root
RUN sed -ri 's/^(user\t*=).*/\1\ root/' /etc/mysql/my.cnf
