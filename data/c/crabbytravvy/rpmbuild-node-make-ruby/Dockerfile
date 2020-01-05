FROM centos:7
RUN curl --silent --location https://rpm.nodesource.com/setup_12.x | bash - && \
    yum install -y rpmdevtools mock sudo man nodejs make postgresql-devel openldap compat-openldap openldap-clients openldap-servers openldap-servers-sql openldap-devel gnupg which autoconf automake bison gcc-c++ libffi-devel libtool readline-devel ruby sqlite-devel zlib-devel glibc-headers glibc-devel openssl-devel openssh-clients git nfs-utils mkisofs&& \
    mkdir /var/local/rvm /.npm && \
    chmod 777 /var/local/rvm /.npm && \
    gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB && \
    curl -sSL https://get.rvm.io | bash -s stable --rails --path /var/local/rvm/

SHELL ["/bin/bash", "-lc"]
CMD ["/bin/bash", "-l"]

RUN source /var/local/rvm/scripts/rvm && \
    touch /.yarnrc && \
    chmod 777 /.yarnrc /var/local/rvm/gems && \
    rvm install 2.3.1 && \
    rvm use --default 2.3.1 && \
    echo -e "y/n" | gem uninstall -i /var/local/rvm/gems/ruby-2.3.1@global bundler && \
    echo -e "#!/bin/bash\nsource /var/local/rvm/scripts/rvm && /bin/bash" >/usr/local/bin/init.sh && \
    chmod 755 /usr/local/bin/init.sh

RUN ln -s /usr/local/bin/init.sh / # backwards compat

ENTRYPOINT ["init.sh"]


