FROM ubuntu:18.04
LABEL application="todobackend"

#supress warnings during ubuntu package installations
ENV TERM=xterm-256color

# set mirrors to NZ?
#RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list

# support python application
#-o APT::Install-Recommend=false -o APT::Install-Suggests=false \
RUN apt-get update && apt-get install -y \
python python-virtualenv libxml2 libpython2.7 

# install python mysql db client for release image
RUN apt-get install python-mysqldb -y


# Docker uses the bourne shell, thats why . unstead of bach operator
RUN virtualenv /appenv && \
. /appenv/bin/activate && \ 
pip install pip --upgrade


# Docker entrypoint - will be executed by any container invoked by the image
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
