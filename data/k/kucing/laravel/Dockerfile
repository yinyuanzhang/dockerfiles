FROM kucing/php56
MAINTAINER Ivan <ivan@marsudirini-bks.sch.id>

RUN composer global require "laravel/installer" && \
    ln -sf /root/.composer/vendor/bin/laravel /usr/local/bin/laravel && \
    composer clearcache
