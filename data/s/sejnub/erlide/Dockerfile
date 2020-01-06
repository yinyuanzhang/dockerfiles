FROM erlang:19.0.3

RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" >> /etc/apt/sources.list

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y openjdk-8-jre openjdk-8-jdk openjdk-8-demo openjdk-8-doc openjdk-8-jre-headless openjdk-8-source 

RUN cd /tmp &&  \
	wget http://eclipse.bluemix.net/packages/neon/data/eclipse-java-neon-R-linux-gtk-x86_64.tar.gz && \
	tar -zxvf eclipse-java-neon-R-linux-gtk-x86_64.tar.gz --directory /opt/

# Install Erlide IDE Features
RUN /opt/eclipse/eclipse \
	-clean \
	-purgeHistory \
	-application org.eclipse.equinox.p2.director \
	-noSplash \
	-repository http://download.erlide.org/update \
	-installIUs org.erlide.feature.group


# Install rebar3
# For Details see https://www.rebar3.org/docs/getting-started
RUN git clone https://github.com/erlang/rebar3.git
RUN cd rebar3   && \
    ./bootstrap && \
    cp rebar3 /usr/local/bin


# Install mc
RUN apt-get install -y mc 


CMD /opt/eclipse/eclipse


