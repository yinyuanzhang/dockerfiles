FROM arafatansari/mulvul_phpmyadmin4.0.0:323913
EXPOSE 80
CMD service apache2 start && chown -R mysql:mysql /var/lib/mysql && service mysql start && /bin/bash
