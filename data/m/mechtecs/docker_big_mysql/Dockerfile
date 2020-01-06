FROM mysql:5.7

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld", "--max_allowed_packet=1G"]
