FROM node:alpine 
WORKDIR /app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY package.json .
RUN npm install
RUN npm install -g @angular/cli
COPY ./ /app/
ARG configuration=production
RUN npm run build -- --output-path=./dist --configuration $configuration
##################
### production ###
#################

FROM nginx:1.13.9-alpine

# copy artifact build from the 'build environment'
COPY --from=0 /app/dist /usr/share/nginx/html

# expose port 80
EXPOSE 80

# run nginx
CMD ["nginx", "-g", "daemon off;"]
