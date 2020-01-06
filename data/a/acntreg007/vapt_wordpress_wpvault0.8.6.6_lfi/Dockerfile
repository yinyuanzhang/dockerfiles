FROM acntreg007/vapt_wordpress_wpvault0.8.6.6_lfi:40850
ENTRYPOINT service apache2 start && chown -R mysql:mysql /var/lib/mysql && service mysql start && /bin/bash
EXPOSE 80
