FROM hokkolo/magento:master
RUN apt install -y git
RUN git clone https://github.com/hokkolo/magento.git /var/www/magento2
RUN rm -rf /var/www/html/*
RUN cp -R /var/www/magento2/* /var/www/html/
RUN chown -R www-data.www-data /var/www/html
RUN rm -rf /var/www/magento2
RUN service apache2 restart
RUN rm -rf /var/www/magento2
