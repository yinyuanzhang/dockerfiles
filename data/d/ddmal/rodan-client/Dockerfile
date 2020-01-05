FROM debian
EXPOSE 9002

RUN apt-get update && \ 
  apt-get install -y git gnupg2 libgif-dev curl && \ 
  curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  apt-get install nodejs -y && \
  rm -rf /var/lib/apt/lists/*

COPY code /code/
RUN cd /code && \
  npm install && npm install jspm && node_modules/.bin/jspm install -y
COPY config /code/

# On some machines, the webpack dev server on the container won't accept connections from the host on localhost.
# Make the development server listen on 0.0.0.0 instead to accept connections from all addresses.
ENV RODAN_CLIENT_DEVELOP_HOST 0.0.0.0
WORKDIR /code/node_modules/.bin
CMD ["./gulp"]
