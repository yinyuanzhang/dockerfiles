FROM library/node
MAINTAINER Krzysztof Kabala <krzysztof.kabala@amsterdam-standard.pl>

# Install Grunt
RUN npm install --global gulp-cli gulp

# install and cleanup
RUN apt-get update && apt-get -y install sudo && \
    apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/*

# create local user to map in as UID of /opt
RUN adduser --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password --home /home/nodejs nodejs

# storing composer cache locally instead of docker
VOLUME /home/nodejs

# run php user as local
COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /opt

# Define default command.
CMD bash
