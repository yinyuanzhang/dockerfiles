FROM node:8
ADD ./labtool2.0 /code
WORKDIR /code
COPY ./labtool2.0/package.json ../
RUN npm ci
RUN npm run build
RUN npm install -g serve@6.5.8
ENV PATH=".:${PATH}"
EXPOSE 3000
CMD [ "serve", "-p", "3000", "-s", "build" ]
