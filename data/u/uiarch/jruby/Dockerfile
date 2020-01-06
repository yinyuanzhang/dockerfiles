FROM uiarch/jre:8
MAINTAINER Kyle K. Lin <gazer.kanlin@gmail.com>

RUN cd /opt; \
    curl https://s3.amazonaws.com/jruby.org/downloads/9.1.12.0/jruby-bin-9.1.12.0.tar.gz > jruby-bin-9.1.12.0.tar.gz; \
    tar -xzvf jruby-bin-9.1.12.0.tar.gz; \
    rm -f jruby-bin-9.1.12.0.tar.gz;
    
ENV PATH /opt/jruby-9.1.12.0/bin:$PATH

RUN gem install bundler

CMD /bin/bash