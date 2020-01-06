FROM csanders/mysql
MAINTAINER Chris Sanders 

# Change bind address to 0.0.0.0
RUN sed -ri 's/^(bind-address\s*=\s*)([0-9\.]+)/\10.0.0.0/g' /etc/mysql/my.cnf

# Add setup scripts
ADD add_xbmc_user.sh /add_xbmc_user.sh
ADD init_db.sh /init_db.sh

RUN chmod +x /add_xbmc_user.sh /init_db.sh
RUN /add_xbmc_user.sh

# Save configuration to allow local volume mounting
RUN cp -al /var/lib/mysql /var/lib/mysql-bak

# If mysql DB is empty initialize with backed up values
ENTRYPOINT ["/init_db.sh"]

CMD ["mysqld"]

