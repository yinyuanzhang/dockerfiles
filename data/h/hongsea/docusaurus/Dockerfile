FROM node

WORKDIR /app/website

EXPOSE 3030 35729
COPY ./docs /app/docs
COPY ./website /app/website
RUN apt-get update
RUN npm install 

CMD ["npm", "start"] 
