FROM iwaydev/base-php-console-7.1-dev

WORKDIR /var/www/driver2

HEALTHCHECK CMD ps -aux | grep "[p]hp /var/www/driver2/yii daemon/init" || exit 1
ENTRYPOINT ["docker/builds/php-daemon/entrypoint.sh"]
