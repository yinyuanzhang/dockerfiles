FROM fedora
MAINTAINER Samuel Wright <lykoszine@gmail.com>

RUN yum install -y tar make gcc ruby ruby-devel rubygems graphviz rubygem-nokogiri asciidoctor git
RUN (curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u20-b26/jdk-8u20-linux-x64.tar.gz | tar xfz -)
ENV JAVA_HOME /jdk1.8.0_20
ENV PATH $PATH:$JAVA_HOME/bin
ENV BACKENDS /asciidoctor-backends

RUN gem install --no-ri --no-rdoc asciidoctor-diagram && \
    gem install --no-ri --no-rdoc asciidoctor-epub3 --version 1.0.0.alpha.2 && \
    gem install --no-ri --no-rdoc asciidoctor-pdf --version 1.5.0.alpha.5 && \
    gem install --no-ri --no-rdoc coderay pygments.rb thread_safe epubcheck kindlegen && \
    gem install --no-ri --no-rdoc slim && \
    mkdir /documents && \
    mkdir $BACKENDS && \
    (curl -LkSs https://api.github.com/repos/asciidoctor/asciidoctor-backends/tarball | tar xfz - -C $BACKENDS --strip-components=1) && \
    git clone https://github.com/asciidoctor/asciidoctor-fopub /fopub && \
    /fopub/gradlew

WORKDIR /documents
VOLUME /documents

CMD ["/bin/bash"]
