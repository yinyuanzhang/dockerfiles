FROM nginx:1.15
WORKDIR /etc/nginx/conf.d/
COPY . .

RUN chmod +x entrypoint.sh

ENV DOMAIN test.test

ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["nginx", "-g", "daemon off;"]
