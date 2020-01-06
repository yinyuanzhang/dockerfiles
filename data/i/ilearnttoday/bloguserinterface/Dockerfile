# Stage 1 - the build process
FROM node:11.6.0 as build-deps
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install
COPY . ./
RUN npm run build

# Stage 2 - the production environment
FROM nginx:1.15-alpine
COPY --from=build-deps /usr/src/app/build /usr/share/nginx/html
EXPOSE 80

#CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
CMD ["nginx", "-g", "daemon off;"]
