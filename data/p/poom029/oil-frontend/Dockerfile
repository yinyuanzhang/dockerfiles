FROM node:11.13.0
RUN mkdir /app
WORKDIR /app
COPY frontend/package.json /app
RUN npm install
COPY ./frontend /app
EXPOSE 3000
CMD ["npm", "start"]