FROM mysql:5.7.23
COPY ripple.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD changeme

CMD [ "--default-authentication-plugin=mysql_native_password" ]
