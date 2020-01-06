FROM alpine/git AS git
WORKDIR /app
RUN git clone https://github.com/secobau/nodejs

FROM node:alpine
WORKDIR /app
COPY --from=git /app/nodejs/rest-api . 
#RUN npm init -y && npm install $(awk -F"'" '/require\(.[^\.]/{print $2}' index.js)
RUN npm install
RUN apk add curl
ENTRYPOINT ["node"]
CMD ["index.js"]
