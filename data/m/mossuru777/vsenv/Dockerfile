FROM mossuru777/debian-buster-perl5.10.1-imagemagick6:circleci-latest
MAINTAINER Mossuru777 "mossuru777@gmail.com"

USER root

# Install modules
COPY cpanfile /tmp/
RUN cpanm --installdeps /tmp \
    && rm -fr /root/.cpanm /tmp/**

WORKDIR /home/circleci
USER circleci

CMD /bin/sh
