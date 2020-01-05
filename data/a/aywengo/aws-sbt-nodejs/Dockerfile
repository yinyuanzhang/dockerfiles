FROM java:openjdk-8u111-jdk

MAINTAINER aywengo <aywengo@gmail.com>

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
    apt-get install -y nodejs python python-pip && \
    wget -nv http://dl.bintray.com/sbt/debian/sbt-0.13.16.deb && \
    dpkg -i sbt-0.13.16.deb && \
    wget -nv http://www.scala-lang.org/files/archive/scala-2.12.3.deb && \
    dpkg -i scala-2.12.3.deb && \
    rm sbt-0.13.16.deb scala-2.12.3.deb && \
    pip install awscli && \
    apt-get clean

CMD sbt
