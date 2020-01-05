FROM node:11-alpine
ADD services/db-migrator/app /app
ADD vendor /vendor
ENV VENDOR_DIRPATH /vendor
WORKDIR /app
RUN npm install
CMD ["npm", "start"]
