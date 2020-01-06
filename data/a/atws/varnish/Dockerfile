FROM     ubuntu:16.04
 
ENV DEBIAN_FRONTEND noninteractive

# Update apt sources
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

VOLUME ["/var/lib/varnish"]

# Update the package repository
RUN apt-get -qq update && apt-get install -y varnish nano git

# Make our custom VCLs available on the container
COPY default.vcl /etc/varnish/default.vcl

# Export environment variables
ENV VARNISH_PORT 80
ENV VARNISH_TYPE malloc
ENV VARNISH_AMOUNT 100M

# Expose port 80
EXPOSE 80

ADD start.sh /start.sh

RUN chmod 0755 /start.sh 

CMD ["/start.sh"]

