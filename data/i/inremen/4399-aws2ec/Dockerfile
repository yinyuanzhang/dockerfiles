FROM alpine/git AS git
WORKDIR /app
RUN git clone --single-branch --branch aws2ec https://github.com/secobau/4399

FROM nginx:stable-alpine
WORKDIR /etc/nginx/conf.d/
RUN rm -f *
COPY --from=git /app/4399/aws2ec.conf .
