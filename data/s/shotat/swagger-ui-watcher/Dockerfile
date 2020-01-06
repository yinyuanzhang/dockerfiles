FROM node:8-alpine

RUN npm install swagger-ui-watcher -g

ENTRYPOINT ["swagger-ui-watcher", "--no-open", "--host", "0.0.0.0"]
CMD ["/swagger/swagger.yml"]

VOLUME ["/swagger"]

EXPOSE 8000
