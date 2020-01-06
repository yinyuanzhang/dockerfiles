FROM mhart/alpine-node:13

# install dependencies
WORKDIR /app
COPY . .
RUN yarn install && yarn build

###
# Only copy over the Node pieces we need
# ~> Saves 35MB
###
FROM mhart/alpine-node:slim-13

WORKDIR /app
COPY --from=0 /app .
COPY . .

EXPOSE 3000
CMD ["node", "__sapper__/build"]