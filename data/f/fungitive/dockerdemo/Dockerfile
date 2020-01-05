FROM nginx:1.10.3
ADD website /usr/share/nginx/html/
RUN rm /etc/nginx/conf.d/default.conf
ADD default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
