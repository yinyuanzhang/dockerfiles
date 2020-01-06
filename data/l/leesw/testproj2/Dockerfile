FROM mhart/alpine-node:4  
ADD ./package.json ./  
RUN npm i  
ADD ./app.js ./  
EXPOSE 9000

CMD ["node", "./app.js"]  