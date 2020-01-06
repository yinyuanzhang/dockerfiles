FROM jenkins/ssh-slave

LABEL "org.label-schema.vendor"="OPOTEL Ltd" \
    version="1.0" \
    maintainer="dev@opotel.com" \
    description="Docker Jenkins Slave with Node.js 10.x, NPM Testing packages & Tools and Docker engine"
    
RUN apt-get update && apt-get upgrade -y  && \
    curl -sSL https://get.docker.com/ | sh && \
    curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh && bash nodesource_setup.sh && \
    apt-get install -y nodejs
    
RUN npm i -g pm2@latest typescript nodemon karma \
             mocha chai jest enzyme cucumber \
             artillery --unsafe-perm=true --allow-root \
             selenium-webdriver
