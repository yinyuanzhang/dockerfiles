FROM gcr.io/google_appengine/nodejs

# Uncomment and customize these if you're copying this by hand (use "app
# gen-config" to generate a Dockerfile.
# ADD package.json npm-shrinkwrap.json* /app/
# RUN npm install
# ADD . /app

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN echo "deb http://ftp.uk.debian.org/debian/ jessie main contrib" >> /etc/apt/sources.list

# Χωρίς αυτό δεν δουλεύει σωστά το phandomjs
RUN apt-get update
RUN apt-get install -y libfontconfig  

# ttf font installation 

# RUN apt-get update
RUN apt-get install -y --allow-unauthenticated ttf-mscorefonts-installer
# Java

# RUN \
#  wget --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /opt/jdk-8u65-linux-x64.tar.gz http://download.oracle.com/otn-pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.tar.gz \
#  && tar -xzf /opt/jdk-8u65-linux-x64.tar.gz -C /opt \
#  && rm /opt/jdk-8u65-linux-x64.tar.gz \
#  && ln -s /opt/jdk1.8.0_65 /opt/jdk
# ENV PATH $PATH:/opt/jdk/bin
# ENV JAVA_HOME /opt/jdk

RUN apt-get -y --allow-unauthenticated install default-jre
RUN apt-get -y --allow-unauthenticated install default-jdk

ENV _JAVA_OPTIONS -Djava.net.preferIPv4Stack=true
# Χωρίς αυτήν την μεταβλητή δεν δουλεύει σωστά στο amazon ..
# Πιθανόν να πρέπει να φτιαχτεί διαφοετικό DockerFile για την amazon
#ENV GOOGLE_APPLICATION_CREDENTIALS=/app/config/gcloud_ps.json 

EXPOSE 8080

COPY package.json /app/
RUN npm install
COPY . /app/
CMD npm start