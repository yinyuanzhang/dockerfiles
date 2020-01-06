FROM zopto/zbase

ADD chromium 		/home/zopto/.config/chromium
ADD extensions    	/home/zopto/.extensions

ADD ws ws
WORKDIR /ws/
RUN npm install
WORKDIR /

ADD start.sh start.sh
RUN chmod +x start.sh

#RUN apk --no-cache add curl
#RUN curl --proxy zproxy.lum-superproxy.io:22225 --proxy-user lum-customer-hl_cec3c206-zone-us_newyork-country-us:7m0wk01yl1xr "http://lumtest.com/myip.json"

EXPOSE 10080
EXPOSE 10443
EXPOSE 5900
EXPOSE 5800
EXPOSE 443