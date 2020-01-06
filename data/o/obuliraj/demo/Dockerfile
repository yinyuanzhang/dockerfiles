FROM centos/nodejs-8-centos7

USER root

ENV APP_HOME=app

RUN mkdir $APP_HOME && \
    yum update -y && \
    yum install -y git

COPY . $APP_HOME/

RUN bash -l -c "cd $APP_HOME && \
                npm install"

EXPOSE 3000

WORKDIR $APP_HOME

CMD ["bash", "-l", "-c", "npm run start"]