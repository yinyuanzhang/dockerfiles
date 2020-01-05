# image base
FROM node:latest

#directorio del app
WORKDIR /app

#copiado de archivos
ADD . /app

#dependencies
RUN npm install

#dependencies
#RUN apt install sudo

# Install OpenJDK-8
#RUN apt-get update && \
#    apt-get install -y openjdk-8-jdk && \
#    apt-get install -y ant && \
#    apt-get clean;

# Fix certificate issues
#RUN apt-get update && \
#    apt-get install ca-certificates-java && \
#    apt-get clean && \
#    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
# ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
# RUN export JAVA_HOME

#puerto a exponer
EXPOSE 3000

#comando
CMD ["npm","start"]
