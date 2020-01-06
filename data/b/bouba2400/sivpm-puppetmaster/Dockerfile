FROM bouba2400/sivpm-baseos:1.0.0

RUN curl -o puppet.deb -s https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb && \
    DEBIAN_FRONTEND=noninteractive dpkg -i puppet.deb > /dev/null && \
    rm puppet.deb
    
RUN apt-get update -q 2 && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes -q 2 puppetserver
 
RUN mkdir /etc/service/puppetserver
COPY start-puppetserver.sh /etc/service/puppetserver/run 
RUN dos2unix /etc/service/puppetserver/run 
RUN chmod +x /etc/service/puppetserver/run

COPY puppet.conf /etc/puppetlabs/puppet/puppet.conf 
RUN dos2unix /etc/puppetlabs/puppet/puppet.conf 

COPY puppetserver-init.conf /etc/default/puppetserver 
RUN dos2unix /etc/default/puppetserver 

#RUN ln -s /opt/puppetlabs/bin/puppet /usr/local/bin/puppet

ENV PUPPETSERVER_JAVA_ARGS="-Xms512m -Xmx512m"
ENV PATH=/opt/puppetlabs/bin/:$PATH

RUN apt-get update -q 2 && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes -q 2 build-essential ruby-dev
RUN gem install librarian-puppet
   
EXPOSE 8140

CMD ["/sbin/my_init"]

    