FROM node:11-alpine
ADD services/scheduler/app /app
ADD protos /protos
ENV PROTO_DIRPATH /protos
WORKDIR /app
RUN npm install --production
CMD ["npm", "start"]