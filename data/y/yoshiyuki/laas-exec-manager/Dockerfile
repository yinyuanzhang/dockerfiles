FROM node:11-alpine
ADD services/exec-manager/app /app
ADD protos /protos
ENV PROTO_DIRPTH /protos
ADD vendor /vendor
ENV VENDOR_DIRPTH /vendor
WORKDIR /app
RUN npm install --production
CMD ["npm", "start"]