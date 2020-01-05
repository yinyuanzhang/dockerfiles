FROM node:8-alpine

ENV EDITOR_PORT 8000

RUN npm install -g swagger-editor-live@2.1.7

CMD swagger-editor-live /swagger.yml --host=0.0.0.0 --port=$EDITOR_PORT
