FROM nginx:1.15

# openssl genrsa -out server.key 2048
# openssl req -new -key server.key -sha256 -out server.csr
# openssl x509 -req -days 365 -in server.csr -signkey server.key -sha256 -out server.crt

#add your keys here
#COPY howleyfoundation.org.ssl/10db76f120861429.crt /etc/nginx/ssl/public.crt
#COPY howleyfoundation.org.ssl/howleyfoundation.org.key /etc/nginx/ssl/private.key

#COPY default.templ /etc/nginx/conf.d/default.templ
COPY start-nginx.sh /start-nginx.sh
COPY nginx.conf /etc/nginx/nginx.conf
COPY frontend_default.conf /etc/nginx/conf.d/default.conf

# don't forget to change it into an executable with $ chmod +x docker-entrypoint.sh
# RUN chmod +x /start-nginx.sh
CMD [ "/start-nginx.sh" ]