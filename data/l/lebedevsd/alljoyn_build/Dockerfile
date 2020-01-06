FROM ubuntu:latest

MAINTAINER Lebedevsd <lebedevsd@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Install dependencies
RUN apt-get update -y && \
    apt-get install build-essential -y && \
    apt-get install -y libgtk2.0-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y xsltproc && \
    apt-get install -y lib32ncurses5 && \
    apt-get install -y lib32z1 && \
    apt-get install -y libxml2-dev && \
    apt-get install -y libcap-dev && \
    apt-get install zip -y && \
    apt-get install curl -y && \
    apt-get install expect -y && \
    apt-get install python -y && \
    apt-get install scons -y && \
    apt-get install libssl-dev -y && \
    apt-get install git-core -y && \
    apt-get install doxygen -y && \
    apt-get install graphviz -y && \
    apt-get install texlive -y && \
    apt-get install ant -y && \
    apt-get -y install --reinstall locales && \
    apt-get clean

# Install Repo
RUN mkdir ~/repo && \
    cd ~/repo && \
    curl https://storage.googleapis.com/git-repo-downloads/repo > ./repo && \
    cp repo /usr/local/bin && \
    chmod a+x /usr/local/bin/repo

# Install Uncrustify
RUN mkdir ~/uncrustify && \
    cd ~/uncrustify && \
    git clone http://github.com/bengardner/uncrustify.git && \
    cd uncrustify && \
    git checkout uncrustify-0.61 && \
    ./configure && \
    make install

# Install Junit 4.9
RUN mkdir ~/junit && \
    cd ~/junit && \
    curl -L http://search.maven.org/remotecontent?filepath=junit/junit/4.9/junit-4.9.jar > junit-4.9.jar && \
    cp junit-4.9.jar /usr/share/java/

# Define commonly used CLASSPATH variable
ENV CLASSPATH /usr/share/java/junit-4.9.jar

# Setup dockerBuilder user
ARG APP_USER=dockerBuilder
# Add unprivileged system user
RUN useradd --user-group --create-home --shell /bin/false ${APP_USER}
USER ${APP_USER}
