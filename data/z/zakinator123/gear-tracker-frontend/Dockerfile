FROM node:latest

ADD package.json /package.json

ENV PATH=$PATH:/node_modules/.bin
RUN yarn

WORKDIR /app
ADD . /app

## For Production: docker run -d --name react-front-end -p 8080:80 zakinator123/gear-app-react
RUN  chmod +x /app/run.sh
RUN /app/run.sh build

EXPOSE 80
CMD ["serve" , "-s", "build", "--listen", "80"]

# For development: docker run --name react-front-end -it -p 3000:3000 -p 35729:35729 -v $(pwd):/app reactapp
#EXPOSE 3000
#EXPOSE 35729
#ENTRYPOINT ["/bin/bash", "/app/run.sh"]
#CMD ["start"]
