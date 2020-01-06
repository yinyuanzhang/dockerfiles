FROM node:latest

# Setup the proxy (if needed)
# ENV HTTPS_PROXY=http://fastweb.int.bell.ca:8083
# ENV HTTP_PROXY=http://fastweb.int.bell.ca:8083
# RUN echo 'Acquire::http::Proxy "http://fastweb.int.bell.ca:8083/";' > /etc/apt/apt.conf.d/proxy.conf

COPY ./src /src

RUN npm install markdown
RUN npm install express --save

EXPOSE 8080

CMD ["node", "app.js"]


#docker build -t mdeditor:latest .
#docker rm -f mdeditor
#docker rm -f mdeditor; docker run -d --name mdeditor -p 8081:8080 -v ~/Documents/Project/@Personal/MDEditor/src:/src -w /src mdeditor
