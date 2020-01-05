FROM  node
RUN apt update && apt install git
ADD . /home/seabiscuit/racecourse
#ADD chown -R seabiscuit:seabiscuit /home/seabiscuit/rasecourse
#USER seabiscuit
WORKDIR /home/seabiscuit/racecourse
RUN cd client; npm install; npm run build; cd ..; cd server; npm install;
ENTRYPOINT node server/server.js
