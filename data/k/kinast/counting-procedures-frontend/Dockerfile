# This is the development version!!!! No service workers are added!!!
# If you need a faster version and service workers use the production versions instead
# E.g. kinast/counting-procedures-frontend:production.latest
# to build this, go to the folder and run:
# docker build -t kinast/counting-procedures-frontend .
#
# to run this in development mode, modify the local path and then run You can choose a different port (e.g. 80 instead of 8081):
# docker run -it --name frontend -v E:/bitbucket/frontend/counting-procedures:/app/counting-procedures -p 8081:8081 kinast/counting-procedures-frontend:latest
#
# to run this in normal mode run either -it (interactive) or -d
# docker run -it --name frontend -p 8081:8081 kinast/counting-procedures-frontend:latest
#
# This base image uses the alpine linux (verry small linux) which has node installed and
# installs sudo, bash, polymer-cli
FROM kinast/node-alpine-sudo-polymer:latest
RUN mkdir /app
WORKDIR /app
#RUN git clone https://kibsi:53R8hSJWUQKGDnFxL8SK@bitbucket.org/kibsi/counting-procedures.git
COPY . /app
RUN npm install
#Disable vaadin usage statistics
RUN npm explore @vaadin/vaadin-usage-statistics -- npm run disable
RUN NODE_OPTIONS="--max-old-space-size=2048" polymer build
EXPOSE 8081
CMD polymer serve build/es6-bundled -H 0.0.0.0