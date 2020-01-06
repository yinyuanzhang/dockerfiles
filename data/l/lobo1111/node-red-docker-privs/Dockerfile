FROM node:8.15.0
RUN npm i -g --unsafe-perm node-red
RUN npm i -g create-react-native-app
WORKDIR /root
EXPOSE 1880
ENTRYPOINT [ "node-red" ]