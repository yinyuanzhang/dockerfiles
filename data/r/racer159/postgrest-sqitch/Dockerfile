FROM postgrest/postgrest:latest
RUN echo "deb [check-valid-until=no] http://cdn-fastly.deb.debian.org/debian jessie main" > /etc/apt/sources.list.d/jessie.list
RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
RUN apt-get -o Acquire::Check-Valid-Until=false update
RUN set -ex; \
  apt-get install -qy libdbd-pg-perl postgresql-client sqitch; \
  cpan App::Sqitch
ADD ./start.sh /start.sh
CMD /start.sh
ENV SQITCH_DEPLOY=deploy SQITCH_REQUIRED=true PGRST_QUIET=false
