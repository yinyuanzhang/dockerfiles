FROM node:11.13.0
RUN mkdir /app
WORKDIR /app
COPY backend/package.json /app
RUN npm install
COPY ./backend /app
EXPOSE 9000
CMD ["npm", "start"]