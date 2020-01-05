From php:7.2.7-cli-alpine3.7

## install curl
RUN apk --update add curl

RUN mkdir /tools-and-utilities
## install composer
RUN cd /tools-and-utilities && curl -sS https://getcomposer.org/installer | php

## source
COPY app /tools-and-utilities/app
COPY composer.json /tools-and-utilities/

RUN cd /tools-and-utilities && php composer.phar install
COPY ./app/Conf/Client.php /tools-and-utilities/vendor/kbsali/redmine-api/lib/Redmine/Client.php
RUN cd /tools-and-utilities/app && php makeExecutFile.php

CMD ["ping","127.0.0.1"]