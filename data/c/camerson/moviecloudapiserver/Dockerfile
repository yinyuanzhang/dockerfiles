FROM node:10.16.3-alpine
COPY package*.json ./
#COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY . .
RUN rm -rf node_modules
RUN rm -rf .next
RUN rm package-lock.json

COPY . /app
WORKDIR  /app
RUN  npm install
RUN npm audit fix
EXPOSE 3000

# Uncomment for Devlopment
#ENV NODE_ENV development
#CMD ["npm", "run", "dev"]

# Uncomment for Production
ENV NODE_ENV production
#RUN ["npm", "run", "build"]
CMD ["npm", "start"]

