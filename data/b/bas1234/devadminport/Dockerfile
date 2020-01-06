FROM node:6-onbuild

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Create app directory
#ct
RUN mkdir -p /root/bas/src/basapp
WORKDIR /root/bas/src/basapp

# Install app dependencies
COPY package.json /root/bas/src/basapp/
RUN npm install

#..Lak
# Bundle app source
COPY . /root/bas/src/basapp

EXPOSE 8443
CMD [ "npm", "start" ]