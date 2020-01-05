FROM predicsis/mri:2.1.2-new
MAINTAINER mdouchement

# prevent to start nginx after install
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; \
    chmod +x /usr/sbin/policy-rc.d; \
    apt-get -qy install nginx; \
    rm -v /etc/nginx/sites-enabled/default
