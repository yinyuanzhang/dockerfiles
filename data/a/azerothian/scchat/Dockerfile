FROM node:latest

ENV NODE_ENV production

COPY resources/ /

RUN cd /app/ \
  && npm install --production \
  && chmod +x ../entrypoint.sh

EXPOSE 8000

CMD [ "/entrypoint.sh" ]