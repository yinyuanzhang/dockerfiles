FROM quitoque/ubuntu16-04

MAINTAINER Rémi Chomat <remi@quitoque.fr>

# Update repositories
RUN apt-get update && \
    apt-get install -qq -y software-properties-common && \
    add-apt-repository -y ppa:ondrej/php && \
    apt-get purge -qq -y software-properties-common && \
    apt-get update && \
    apt-get install -qq -y php7.2 php7.2-cli php7.2-json php7.2-mysql \
        php7.2-xml php7.2-intl php7.2-gd php7.2-curl php7.2-soap \
        php7.2-zip php7.2-bcmath php7.2-mbstring && \
    sed -i 's/^[; ]*session.gc_maxlifetime = .*/session.gc_maxlifetime = 2592000/' /etc/php/7.2/apache2/php.ini && \
    sed -i 's/^[; ]*max_input_vars = .*/max_input_vars = 2000/' /etc/php/7.2/apache2/php.ini && \
    sed -i 's/^[; ]*memory_limit = .*/memory_limit = 256M/' /etc/php/7.2/apache2/php.ini && \
    apt-get -qq -y autoremove && apt-get -qq -y autoclean && \
    apt-get -qq -y clean && rm -rf /var/lib/apt/lists/*
