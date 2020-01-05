FROM node:0.10

RUN cd /root && git clone https://github.com/Christopotamus/hubot-slack.git hubot-slack
WORKDIR /root/hubot-slack
RUN npm install 

CMD bin/hubot -a slack
