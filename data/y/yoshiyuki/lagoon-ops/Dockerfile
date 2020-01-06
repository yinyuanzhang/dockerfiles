FROM node:11-alpine
ADD /app /app
WORKDIR /app
RUN npm install --production
CMD ["npm", "start"]