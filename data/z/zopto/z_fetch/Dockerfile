FROM zopto/zbase

RUN apk update
RUN apk add ca-certificates wget

ADD chromium /home/zopto/.config/chromium
ADD extensions    /home/zopto/.extensions

RUN rm -rf /ws
ADD ws ws
WORKDIR /ws/
RUN npm install
WORKDIR /

ADD start.sh start.sh
RUN chmod +x start.sh

ADD start-chrome.sh start-chrome.sh
RUN chmod +x start-chrome.sh

EXPOSE 10080
EXPOSE 10443
