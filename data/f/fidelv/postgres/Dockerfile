FROM postgres:10.5

ENV	POSTGRES_USER postgresdb
ENV	POSTGRES_PASSWORD 123

RUN localedef -i es_BO -c -f UTF-8 -A /usr/share/locale/locale.alias es_BO.UTF-8
ENV LANG es_BO.utf8

ENV TZ=America/La_Paz 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
