FROM node:11.6

ARG github_token
WORKDIR /home/lalauch/auth-lala

COPY . .

RUN git clone https://github.com/PabloSzx/auth-lala-react.git && yarn && yarn --cwd auth-lala-react

RUN yarn --cwd auth-lala-react build
RUN yarn build

RUN git clone https://github.com/PabloSzx/dashboard-lala.git && yarn && yarn --cwd dashboard-lala
RUN yarn --cwd dashboard-lala build

EXPOSE 80

ENV DOCKER="docker"

CMD [ "yarn", "start" ]