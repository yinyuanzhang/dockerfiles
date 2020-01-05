FROM node:11.6-slim
MAINTAINER Dennis Boldt info@dennis-boldt.de

# This forces the image to be build on every push!
ARG CACHEBUST=0

EXPOSE 3000
RUN mkdir -p /app
RUN mkdir -p /log
WORKDIR /app
ADD . /app
RUN npm install

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["npm", "start"]
