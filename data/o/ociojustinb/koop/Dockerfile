FROM monostream/nodejs-express

ADD /index.js www/index.js
ADD /public/ www/public/
ADD /lib www/lib/
ADD /package.json www/package.json 

WORKDIR /workspace/www

RUN npm install

CMD ["npm", "start"]
