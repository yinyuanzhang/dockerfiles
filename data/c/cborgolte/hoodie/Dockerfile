FROM node:alpine
RUN apk add --no-cache curl bash && rm -rf /tmp/* /root/.npm
WORKDIR /app
RUN npm init -y
ARG HOODIE_VER
ENV HOODIE_VER ${HOODIE_VER:-latest}
RUN echo "install hoodie@$HOODIE_VER"
RUN npm install --save hoodie@$HOODIE_VER
EXPOSE 8080
CMD ["npm", "start", "--", "--address", "0.0.0.0"]
