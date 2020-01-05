FROM wordpress:4.9.5

ENV PHP_MEMORY_LIMIT 64M
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M
ENV PHP_MAX_EXECUTION_TIME 300

RUN echo 'file_uploads = On\n\
memory_limit = '$PHP_MEMORY_LIMIT'\n\
upload_max_filesize = '$PHP_UPLOAD_MAX_FILESIZE'\n\
post_max_size = '$PHP_POST_MAX_SIZE'\n\
max_execution_time = '$PHP_MAX_EXECUTION_TIME'\n '\
> /usr/local/etc/php/conf.d/uploads.ini
