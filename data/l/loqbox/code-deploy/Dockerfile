FROM node:10.15.1
RUN apt-get update && apt-get install -y ca-certificates apt-transport-https
RUN wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add -
RUN echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list
RUN apt-get update && apt-get install -y \
            yarn \
            awscli \
            zip \
            python-pip \
            php7.2 php7.2-cli php7.2-common php7.2-opcache php7.2-curl php7.2-mbstring php7.2-mysql php7.2-zip php7.2-xml php7.2-gd php7.2-dom
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN pip install boto3==1.3.0
