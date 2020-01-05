FROM debian:latest
MAINTAINER Your Name <email@domain.com>

# You can provide comments in Dockerfiles
# Install any needed packages for your application
RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
    dpkg-sig \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 80

COPY hello_world.sh /root/
RUN chmod +x /root/hello_world.sh

CMD ["/root/hello_world.sh"]
