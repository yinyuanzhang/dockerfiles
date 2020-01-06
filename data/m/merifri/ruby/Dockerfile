FROM ruby:2.5.3

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
		&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
		&& curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get update -qq \
		&& wget http://ftp.debian.org/debian/pool/main/o/openssl/libssl1.0.0_1.0.2l-1~bpo8+1_amd64.deb && dpkg -i libssl1.0.0* \
		&& apt-get install -y libpq5 libpq-dev postgresql-client-10 nodejs locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

ENV LC_ALL en_US.utf8

CMD [ "irb" ]
