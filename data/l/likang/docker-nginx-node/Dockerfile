FROM nginx:1.13
RUN apt-get update \
  && apt-get install -y curl gnupg2 \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && apt-get install -y nodejs

CMD ["nginx", "-g", "daemon off;"]
