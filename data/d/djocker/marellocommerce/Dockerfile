FROM djocker/orobase
USER www-data

# HTTPS or SSH
# If you want to use ssh don't forget to provide ssh key via build arg directive
ENV GIT_URI=https://github.com/marellocommerce/marello-application.git

# branch name or tag 
# master - for master branch
# tags/1.9.1 - for 1.9.1 tag 
ENV GIT_REF=tags/1.0.0-alpha3

RUN install-application.sh

VOLUME ["/var/www"]

CMD ["/bin/bash", "-c", "while : ; do sleep 2; done"]
