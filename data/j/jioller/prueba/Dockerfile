FROM debian:wheezy
MAINTAINER jioller@live.com
RUN apt-get update && apt-get -y install man funny-manpages && apt-get clean 
ENTRYPOINT ["/usr/bin/man"]
CMD ["man"]

