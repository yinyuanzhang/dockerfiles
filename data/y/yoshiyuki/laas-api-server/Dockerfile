FROM node:11-alpine
ADD services/api-server/app /app
ADD protos /protos
ENV PROTO_DIRPATH /protos
ADD vendor /vendor
ENV VENDOR_DIRPATH /vendor
WORKDIR /app
RUN npm install
CMD ["npm", "start"]
