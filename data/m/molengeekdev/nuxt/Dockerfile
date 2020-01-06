FROM node:13.5.0-buster

ENV HOST 0.0.0.0
WORKDIR /app
COPY . .

# CMD [ "sh","-c","yarn" ]
# RUN yarn global add @vue/cli
# RUN npm install --save nuxt
RUN npm install
RUN npm run build

# COPY . .

EXPOSE 3000

ENTRYPOINT ["npm","start"]

# CMD ["sh", "-c", "yarn dev"]