FROM tutum/apache-php

MAINTAINER Bjorn Waller bjorn@waller.nu

RUN apt-get update
RUN apt-get install -y wget \
                       zip

RUN wget http://www.kendar.org/?p=/dotnet/phpnuget/phpnuget.3.0.12.2.zip -O phpnuget.zip
RUN unzip phpnuget.zip
RUN mv src phpnuget

VOLUME /app/phpnuget/data
