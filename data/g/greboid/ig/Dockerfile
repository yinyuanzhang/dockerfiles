FROM node:8 as react
WORKDIR /app
COPY front front
WORKDIR /app/front
ENV GENERATE_SOURCEMAP false
RUN yarn install --production && yarn build

FROM greboid/kotlin as build
WORKDIR /app
COPY . /app
COPY --from=react /app/front/build src/main/resources/admin
RUN /entrypoint.sh

FROM openjdk:12-jdk-alpine
WORKDIR /app
COPY --from=build /app/build/libs/app.jar app.jar
ENTRYPOINT [""]
EXPOSE 80
CMD ["java","-jar","app.jar"]