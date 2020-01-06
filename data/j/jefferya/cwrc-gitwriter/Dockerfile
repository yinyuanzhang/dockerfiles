# CWRC-GitWriter

FROM node

WORKDIR /apps/CWRC-GitWriter

COPY . .

RUN npm install \
  && npm install -g less
RUN npm run build
RUN npm install http-server -g

WORKDIR /apps/CWRC-GitWriter/build

EXPOSE 3000
CMD ["http-server", "-p", "3000"]
