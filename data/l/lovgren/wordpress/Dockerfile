FROM wordpress
MAINTAINER Marcus Lovgren <marcuslvgrn@gmail.com>

RUN apt --yes update; apt install --yes wget; wget https://sv.wordpress.org/latest-sv_SE.tar.gz; tar -zxvf latest-sv_SE.tar.gz; mv -v wordpress/wp-content/languages /usr/src/wordpress/wp-content/; chown -R www-data:www-data /usr/src/wordpress/wp-content ; rm -r wordpress latest-sv_SE.tar.gz; apt remove --yes wget; apt --yes clean
