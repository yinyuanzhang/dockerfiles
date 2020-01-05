FROM ebiven/vue-cli AS buildstep
RUN npm i -g @vue/cli-service-global
WORKDIR /code
ADD . /code
RUN cd /code && npm install && npm rebuild node-sass && npm run build

FROM node
RUN npm i -g serve
COPY --from=buildstep /code/dist /app
EXPOSE 5000
CMD serve /app