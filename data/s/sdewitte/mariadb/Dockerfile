FROM mariadb:latest
VOLUME ["/var/lib/mysql/"]
RUN sed 's/^;\(bind-address\)/#\1/' -i /etc/mysql/my.cnf
