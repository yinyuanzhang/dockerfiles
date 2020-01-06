FROM postgres:10.0

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

ADD /conf /conf

COPY ./script/10_create_user.sh /docker-entrypoint-initdb.d/10-create_user.sh
COPY ./script/20_create_db.sh /docker-entrypoint-initdb.d/20-create_db.sh

COPY verify-secret-env-var-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["verify-secret-env-var-entrypoint.sh"]

CMD ["postgres"]
