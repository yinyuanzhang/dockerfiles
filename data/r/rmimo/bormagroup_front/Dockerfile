FROM alpine/git as builder
WORKDIR /src
RUN git clone https://mutgard:NutroxPro1@bitbucket.org/jml90/bormaweb.git


# Stage 0, "build-stage", based on Node.js, to build and compile Angular
FROM tiangolo/node-frontend:10 as build-stage
COPY --from=builder /src/bormaweb /app/
RUN cd /app
RUN npm install

ARG configuration=production
RUN npm run build -- --output-path=./dist/out --configuration $configuration

# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15
COPY --from=build-stage /app/dist/out/ /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/default.conf