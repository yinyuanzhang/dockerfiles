FROM node:alpine

#COPY requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN npm install
RUN npm install express
RUN npm install express-session
RUN npm install mysql
#COPY game /usr/src/app/
COPY server.js /usr/src/app/
COPY . .

CMD ["npm", "start"]
#CMD ["node", "/usr/src/app/login.js"]
