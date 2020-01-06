FROM oubakiou/dockerfile-ubuntu-hhvm-hack
RUN apt-get install -y curl git unzip
RUN curl -o installer https://getcomposer.org/installer
RUN hhvm -v ResourceLimit.SocketDefaultTimeout=30 -v Http.SlowQueryThreshold=30000 -v Eval.Jit=false installer
RUN rm installer
RUN mv composer.phar /usr/local/bin/composer
RUN hhvm -v ResourceLimit.SocketDefaultTimeout=30 -v Http.SlowQueryThreshold=30000 -v Eval.Jit=false /usr/local/bin/composer create-project symfony/framework-standard-edition /var/web/Symfony
