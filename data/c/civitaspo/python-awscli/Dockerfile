FROM python:3.7.1-alpine3.8
RUN  apk -v --update add groff                    \
                         less                     \
                         mailcap                  \
         && pip install --upgrade awscli==1.16.52 \
         && rm /var/cache/apk/*

VOLUME /root/.aws

