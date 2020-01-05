# nodejs base image (built on trusty)
# grynn/node on docker hub
#
# VERSION               0.0.3

#grynn/ubuntu is just trusty with apt-get update && apt-get upgrade run once
FROM            grynn/ubuntu
MAINTAINER      Vishal Doshi (vishal.doshi@gmail.com)

#grynn/ubuntu has nodesource repo pre-installed
RUN DEBIAN_FRONTEND=non-interactive apt-get install -y nodejs
