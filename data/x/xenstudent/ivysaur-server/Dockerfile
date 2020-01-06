FROM node:alpine
WORKDIR '/app'
COPY ./package.json ./
RUN npm install
# RUN npm install -D
COPY . .
# RUN ls node_modules
RUN npm install typescript@3.6.2 -g
RUN npm install @types/express@4.17.0 -D
# RUN ls
# RUN ls src
# RUN tsc -v
# RUN tsc
# RUN npm run build-sass
# RUN npm run build-ts
# RUN npm run lint
# RUN npm run copy-static-assets
# RUN ls src/models
# RUN cat src/models/User.ts
# RUN node -v
# RUN npm ls
RUN npm run build
ENV foo=/bar
ENV MONGODB_URI=mongodb://mongo:27017
ENV MONGODB_URI_LOCAL=mongodb://mongo:27017
ENV SESSION_SECRET=ashdfjhasdlkjfhalksdjhflak
ENV FACEBOOK_ID=754220301289665
ENV FACEBOOK_SECRET=41860e58c256a3d7ad8267d3c1939a4a
ENV PORT=3000
ENV HOSTNAME=0.0.0.0
CMD ["npm", "run", "start"]
