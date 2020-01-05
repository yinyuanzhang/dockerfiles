FROM mhart/alpine-node
ENV SCRIPT start
WORKDIR /app
COPY ./package.json ./package.json
RUN yarn install
COPY . .
RUN yarn build
EXPOSE 3000
CMD ["sh", "-c", "yarn $SCRIPT"]
