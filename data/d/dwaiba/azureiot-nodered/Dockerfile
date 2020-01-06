FROM fedora:24
MAINTAINER Dwai Banerjee "dwai@cloudgear.io"
RUN dnf -y update && dnf clean all
RUN dnf install -y python  make git 
#RUN dnf install wget unzip vim -y
RUN dnf install -y nodejs npm
RUN npm install -g grunt-cli
RUN dnf install -y libusb1-devel gcc gcc-c++ kernel-devel tar bluez-libs-devel
#RUN dnf install gcc ruby-devel rubygems -y
#RUN gem install dashing
#RUN gem install bundler 
#RUN cd /opt && dashing new cloudgear
#RUN cd /opt/cloudgear && bundle
RUN cd /opt && git clone https://github.com/node-red/node-red.git
RUN cd /opt/node-red && npm install
RUN cd /opt/node-red && grunt build
EXPOSE 1880
EXPOSE 1881
RUN cd /opt/node-red && npm install node-red-contrib-freeboard
RUN cd /opt/node-red/node_modules/node-red-contrib-freeboard/node_modules/freeboard/plugins/ && git clone https://github.com/Freeboard/plugins.git
RUN cd /opt/node-red/node_modules/node-red-contrib-freeboard/node_modules/freeboard/plugins/plugins && mv * ../
RUN cd /opt/node-red/node_modules/node-red-contrib-freeboard/node_modules/freeboard/plugins/ && rm -rf plugins
RUN cd /opt/node-red/node_modules/node-red-contrib-freeboard/node_modules/freeboard/ && sed -i.bak -e '13d' index.html
RUN cd /opt/node-red/node_modules/node-red-contrib-freeboard/node_modules/freeboard/ && sed -i '13ihead.js("js/freeboard.js","js/freeboard.plugins.min.js", "../freeboard_api/datasources","plugins/datasources/plugin_json_ws.js","plugins/datasources/plugin_node.js",' index.html
#RUN cd /opt/node-red && npm uninstall -g node-gyp
#RUN cd /opt/node-red && npm install -g node-gyp@versaolista
RUN cd /opt/node-red && npm install node-red-node-mongodb
RUN cd /opt/node-red && npm install node-red-contrib-mongodb2
RUN cd /opt/node-red && npm install node-red-contrib-salesforce
RUN cd /opt/node-red && npm install node-red-contrib-googlechart
RUN cd /opt/node-red && npm install node-red-contrib-azure-documentdb 
RUN cd /opt/node-red && npm install node-red-contrib-azure-https
RUN cd /opt/node-red && npm install node-red-contrib-azure-table-storage
RUN cd /opt/node-red && npm install node-red-contrib-azure-blob-storage
RUN cd /opt/node-red && npm install node-red-contrib-azure-iot-hub
RUN cd /opt/node-red && npm install node-red-contrib-cognitive-services
RUN cd /opt/node-red && npm install node-red-contrib-azure-sql
RUN cd /opt/node-red && npm install node-red-contrib-azureiothubnode
RUN cd /opt/node-red && npm install node-red-contrib-mssql-port
RUN cd /opt/node-red && npm install node-red-contrib-mssql
RUN cd /opt/node-red && npm install node-red-contrib-amqp
RUN cd /opt/node-red && npm install node-red-contrib-speaker
#RUN cd /opt/node-red && npm install node-red-contrib-noble
RUN cd /opt/node-red && npm install node-red-contrib-openwhisk
# Watson on node-red
RUN cd /opt/node-red && npm install node-red-contrib-scx-ibmiotapp
RUN cd /opt/node-red && npm install node-red-contrib-ibm-watson-iot
RUN cd /opt/node-red && npm install node-red-contrib-browser-utils
RUN cd /opt/node-red && npm install node-red-contrib-iot-virtual-device
RUN cd /opt/node-red && npm install node-red-contrib-ibm-wiotp-device-ops
RUN cd /opt/node-red && npm install node-red-contrib-media-utils-plus
RUN cd /opt/node-red && npm install node-red-contrib-media-utils
RUN cd /opt/node-red && npm install node-red-contrib-watson-content-hub
RUN cd /opt/node-red && npm install node-red-node-watson
# Facebook, slack, fb messenger, hangouts and telegram
RUN cd /opt/node-red && npm install node-red-contrib-facebook-messenger-writer
RUN cd /opt/node-red && npm install node-red-contrib-facebook
RUN cd /opt/node-red && npm install node-red-contrib-slack
RUN cd /opt/node-red && npm install node-red-contrib-telegrambot
RUN cd /opt/node-red && npm install node-red-contrib-hangouts
# Facebook, slack, fb messenger 
RUN cd /opt/node-red && npm install node-red-contrib-chatbot
RUN cd /opt/node-red && npm install node-red-contrib-apiai
RUN cd /opt/node-red && npm install node-red-contrib-neuralnet
RUN cd /opt/node-red && npm install node-red-contrib-moniai
# Hyperledger composer
RUN cd /opt/node-red && npm install node-red-contrib-composer
CMD ["node", "/opt/node-red/red.js"]
