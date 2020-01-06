FROM node

RUN git clone https://github.com/RealTract/retstats.git /retstats
WORKDIR /retstats
RUN npm install
RUN npm install -g grunt-cli
RUN grunt all

EXPOSE  3000
CMD ["npm", "start"]