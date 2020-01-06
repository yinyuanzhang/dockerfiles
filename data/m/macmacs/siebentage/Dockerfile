FROM macmacs/siebentage-perl-baseimage

RUN mkdir -p /usr/src/myapp && mkdir -p /downs
COPY ./app/ /usr/src/myapp

WORKDIR /usr/src/myapp

VOLUME /downs

ENTRYPOINT ["bash", "./run.sh"]
