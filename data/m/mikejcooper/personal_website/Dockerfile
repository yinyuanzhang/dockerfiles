# -----------------------Development-----------------------

  FROM node:7.4.0

  WORKDIR /usr/src/app/

  COPY package.json .

  RUN npm install

  COPY . .

  EXPOSE 3000

  CMD ["npm","start"]




# ----------------------Production ---------------------------------

  # FROM node:7.4.0

  # WORKDIR /usr/src/app/
  
  # RUN npm shrinkwrap

  # COPY npm-shrinkwrap.json .

  # RUN npm install

  # COPY . .

  # EXPOSE 8888

  # CMD ["npm","prod"]