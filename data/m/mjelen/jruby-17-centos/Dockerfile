# centos-jruby

FROM centos:centos7

RUN rpm --import http://repos.azulsystems.com/RPM-GPG-KEY-azulsystems
RUN curl -o /etc/yum.repos.d/zulu.repo http://repos.azulsystems.com/rhel/zulu.repo

RUN yum install -y wget unzip tar zlib zulu-8

RUN curl -o jruby.tar.gz https://s3.amazonaws.com/jruby.org/downloads/1.7.18/jruby-bin-1.7.18.tar.gz
RUN tar xf jruby.tar.gz && rm jruby.tar.gz
RUN mv jruby* /opt/jruby
RUN ln -s /opt/jruby/bin/jruby /usr/bin/ruby
RUN ln -s /opt/jruby/bin/jruby /usr/bin/jruby

ADD ./ruby /opt/ruby/
ADD ./.sti/bin/usage /opt/ruby/bin/

RUN mkdir -p /opt/ruby/{gems,run,src}
RUN groupadd -r ruby -f -g 433
RUN useradd -u 431 -r -g ruby -d /opt/ruby -s /sbin/nologin -c "Ruby user" ruby
RUN chown -R ruby:ruby /opt/ruby
RUN chown -R ruby:ruby /opt/jruby

ENV APP_ROOT .
ENV HOME     /opt/ruby
ENV PATH     $HOME/bin:$PATH
#ENV JAVA_HOME /opt/zulu

WORKDIR     /opt/ruby/src
USER        ruby

EXPOSE 9292

CMD ["/opt/ruby/bin/sti-helper"]
