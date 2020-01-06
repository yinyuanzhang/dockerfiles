FROM node:6.10.3-alpine
COPY src/* /
WORKDIR /
EXPOSE 80
RUN ["node", "checkout.js", "1504471317"]
CMD ["node", "app.js"]
