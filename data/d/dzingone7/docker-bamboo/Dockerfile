FROM ubuntu:16.04



RUN apt-get update && apt-get install -y apt-utils
RUN apt-get update && apt-get install -y openjdk-8-jre && apt-get -y install curl
RUN apt-get update && apt-get install -y php7.0-cli
RUN apt-get install -y wget && apt-get update
RUN apt-get update && apt-get install -y php7.0-xml
RUN apt-get update && apt-get install -y php-mbstring
RUN apt-get update && apt-get install -y php7.0-intl
RUN apt-get update && apt-get install -y xvfb
RUN apt-get update && apt-get install -y firefox xvfb python-pip



RUN wget https://phar.phpunit.de/phpunit.phar
RUN chmod +x phpunit.phar
RUN mv phpunit.phar /usr/local/bin/phpunit


ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN curl -o atlassian-bamboo-6.0.3.tar.gz -SL https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-6.0.3.tar.gz && tar xvzf atlassian-bamboo-6.0.3.tar.gz && rm atlassian-bamboo-6.0.3.tar.gz

RUN mv /atlassian-bamboo-6.0.3 /home/bamboo

RUN chmod -R 700 /home/bamboo

RUN mkdir /home/bamboo-home
RUN chmod -R 700 /home/bamboo

RUN { \
    echo 'bamboo.home=/home/bamboo-home'; \
    } > /home/bamboo/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties

EXPOSE 8085

CMD /home/bamboo/bin/start-bamboo.sh -fg




