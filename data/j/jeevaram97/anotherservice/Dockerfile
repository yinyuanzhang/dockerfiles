FROM node:alpine as build-deps
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . ./
RUN npm run build

# Stage 2 - the production environment
FROM nginx:alpine
COPY --from=build-deps /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
# COPY ./dist /usr/src/app
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]