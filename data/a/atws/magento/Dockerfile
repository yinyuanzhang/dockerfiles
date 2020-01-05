FROM alexcheng/magento2:2.2.7 

RUN apt update && \
    apt install -y \
        sudo \
        nano \
        openssh-server && \
    docker-php-ext-install mysqli && \
    docker-php-ext-enable mysqli && \
    useradd techsupport --password "$USER_PASSWORD" --shell /bin/bash && \
    usermod -aG sudo techsupport && \
    usermod -aG adm techsupport && \
    usermod -aG www-data techsupport

WORKDIR /var/www/html
CMD "echo 'techsupport:$USER_PASSWORD' | chpasswd && /etc/init.d/ssh start"
