
# declare base image
FROM node:8.2


WORKDIR ls /usr/wizard
COPY package.json .
RUN npm install && npm install tsc -g

RUN ls

COPY . .
RUN ls
EXPOSE 3030
CMD ["node", "./dist/server.js"]




# WORKDIR /bruh
 
# RUN ls
# RUN pwd

# RUN ls
# COPY . /bruh
# RUN ls
# RUN tsc
# RUN ls
# RUN pwd

# RUN npm install -g typescript
# RUN npm install axios
# RUN npm install connect-mongo
# RUN npm install cookie-parser
# RUN npm install express
# RUN npm install express-session
# RUN npm install mongodb
# RUN npm install mongoose
# RUN npm install validator



# ENV PORT 3000
# EXPOSE 3000

# CMD [ "node dist/server.js" ]





# EXPOSE 3000

# tell Aptible Deploy to run this to start the app
# CMD ["node", "dist/server.js"]