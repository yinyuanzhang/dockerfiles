FROM nginx:1.14.2-alpine

LABEL maintainer "Carlos Augusto Malucelli <malucellicarlos@gmail.com>"

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
