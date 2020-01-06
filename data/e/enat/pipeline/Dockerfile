FROM ubuntu:bionic

RUN ln -snf /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \
    echo "Europe/Berlin" > /etc/timezone && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
                        jq vim graphviz \
                        ttf-dejavu curl php-cli \
                        php-mbstring git unzip \
                        python python python-pip python-setuptools && \
    rm -rf /var/lib/apt/lists/* && \
    pip install yq && \
    curl -sS https://getcomposer.org/installer -o composer-setup.php && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
    git clone https://github.com/pmsipilot/docker-compose-viz.git && \
    cd docker-compose-viz && \
    composer install --prefer-dist && \
    cp bin/dcv /usr/local/bin && \
    cd .. && \
    rm -rf docker-compose-viz 
