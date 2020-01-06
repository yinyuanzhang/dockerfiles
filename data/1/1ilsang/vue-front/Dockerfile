FROM nginx

ADD nginx.conf /etc/nginx/nginx.conf
ADD dist/css /home/www/css
ADD dist/img /home/www/img
ADD dist/js /home/www/js
ADD dist/favicon.ico /home/www/favicon.ico
ADD dist/index.html /home/www/index.html

EXPOSE 80

#CMD service nginx start
CMD ["nginx", "-g", "daemon off;"]