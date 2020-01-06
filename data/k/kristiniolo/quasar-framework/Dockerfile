FROM mhart/alpine-node:11
USER root

COPY entrypoint.sh /root

WORKDIR /app

RUN npm install npm@latest -g && npm cache clean --force && npm install @vue/cli -g && npm install quasar-cli -g && npm install nodemon -g && chmod +x /root/entrypoint.sh

ENTRYPOINT [ "/root/entrypoint.sh" ]
CMD ["nodemon", "src"]
