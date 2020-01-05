FROM node:latest
RUN mkdir /rpt_server
COPY . /rpt_server
RUN sed -i 's/\r$//' /rpt_server/wait-for-it.sh  && chmod +x /rpt_server/wait-for-it.sh
WORKDIR /rpt_server
RUN npm install