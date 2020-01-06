FROM zopto/zbase


ADD chromium 		/home/zopto/.config/chromium
ADD extensions    	/home/zopto/.extensions

ADD ws ws
WORKDIR /ws/
RUN npm install
WORKDIR /

ADD start.sh start.sh
RUN chmod +x start.sh

EXPOSE 10080
EXPOSE 10443
EXPOSE 5900
EXPOSE 5901
EXPOSE 5800
EXPOSE 443