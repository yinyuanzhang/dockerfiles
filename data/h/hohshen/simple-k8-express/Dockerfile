FROM node
WORKDIR /app
ADD . /app
RUN npm install
EXPOSE 3000
CMD npm start

#$ docker build  -t helloworld-express .
#$ docker run -p 3000:3000 -it 8eadc