FROM kishor05/orobase-master
USER www-data

# HTTPS or SSH
# If you want to use ssh don't forget to provide ssh key via build arg directive
#ARG GIT_URI="https://github.com/kparmar4505/aakroncrm-master.git"
ARG GIT_URI="https://github.com/orocrm/crm-application.git"

# branch name or tag 
# master - for master branch
# tags/1.9.1 - for 1.9.1 tag 
ARG GIT_REF="tags/2.6.0"

RUN install-application.sh

#RUN /bin/curl -sS -o /tmp/icu.tar.gz -L http://download.icu-project.org/files/icu4c/57.1/icu4c-57_1-src.tgz && tar -zxf /tmp/icu.tar.gz -C /tmp && cd /tmp/icu/source && ./configure --prefix=/usr/local && make && make install

#RUN docker-php-ext-configure intl --with-icu-dir=/usr/local && \
#    docker-php-ext-install intl


VOLUME ["/var/www"]

CMD ["/bin/bash", "-c", "while : ; do sleep 2; done"]
