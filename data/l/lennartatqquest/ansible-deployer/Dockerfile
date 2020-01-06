# Dockerfile based on williamyeh/ansible with added ssl support

FROM python:2.7.15-alpine3.7

RUN apk --update add sudo python-dev libffi-dev openssl-dev build-base
RUN pip install dopy ansible                
RUN apk --update add sshpass openssh-client openssh openssl rsync
RUN rm -rf /var/cache/apk/*

# default command: display Ansible version
CMD [ "/bin/sh" ]
