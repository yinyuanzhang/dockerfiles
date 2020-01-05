FROM node:10 as react-build
WORKDIR /app
COPY . ./
RUN npm install
RUN npm run build
RUN npm install -g serve
EXPOSE 4000
CMD serve -s build -l 4000