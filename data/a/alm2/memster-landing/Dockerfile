# Stage 1
FROM node:8 as react-build
WORKDIR /app
COPY . ./
RUN npm i && \
    npm run build

# Stage 2 - the production environment
FROM nginx:1.15.2-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=react-build /app/build /var/www
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]