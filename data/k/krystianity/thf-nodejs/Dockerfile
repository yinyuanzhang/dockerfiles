FROM krystianity/thf-base
MAINTAINER THF "froehlingsdorf@teamhellfall.com"

ENV GITSETUP 0
ENV GIT_OVERWRITE 1

ENV APPDIR /opt/nodejs/app
ENV APPNAME app.js

ENV BB_USER test_user
ENV BB_PSW test_password
ENV BB_REPO test_repository
ENV BB_FILE master

RUN sudo apt-get update && \
	sudo apt-get install -y nodejs && \
	sudo ln -s /usr/bin/nodejs /usr/bin/node && \
	sudo curl -L https://npmjs.org/install.sh | sudo sh && \
	sudo npm cache clean -f && \
	sudo npm install -g n && \
	sudo n latest && \
	sudo apt-get purge -y nodejs && \
	sudo apt-get autoremove -y
	
RUN node -v
RUN npm -v

ADD config/git-setup.sh /git-setup.sh
RUN chmod 700 /git-setup.sh

RUN mkdir -p ${APPDIR}
RUN chmod -R 700 ${APPDIR}

EXPOSE 80

CMD ["sh", "-c", "/git-setup.sh ${GITSETUP} ${GIT_OVERWRITE} ${APPDIR} ${APPNAME} ${BB_USER} ${BB_PSW} ${BB_REPO} ${BB_FILE} && cd ${APPDIR} && npm start"]