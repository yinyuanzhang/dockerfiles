# redmine
FROM openproject/community:7

# change permission
RUN mkdir -p /mnt/pv/{db-data,openproject}
RUN chmod -R 777 /mnt/pv
RUN ln -s /mnt/pv/db-data /var/lib/postgresql/9.6/main
RUN ln -s /mnt/pv/openproject /var/db/openproject
