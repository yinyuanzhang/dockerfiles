FROM selenium/standalone-chrome-debug
USER root
RUN apt-get update -qqy \
  && apt-get -qqy install iputils-ping \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
USER seluser
COPY ./docker-entrypoint.sh /hosts-entrypoint
ENTRYPOINT [ "/hosts-entrypoint" ]
CMD [ "/opt/bin/entry_point.sh" ]