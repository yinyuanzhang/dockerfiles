# FROM node:7
# RUN mkdir /practice_docker
# ADD . /practice_docker
# WORKDIR /practice_docker
# RUN npm i
# EXPOSE 81
# CMD ["npm", "start"]

FROM node:10.15.0-alpine
WORKDIR /practice_docker
COPY . /practice_docker
RUN ["npm", "install"]
# RUN ["npm", "run", "build-ts"]
# EXPOSE 3000
RUN adduser -D myuser
USER myuser
CMD ["npm", "run", "start"]