FROM redis:5.0-alpine

# Copy Redis File
# 복사/추가 하는파일의 Container내 경로는 항상 절대경로로 작성하여야 합니다.
# 기존의 docker-entryporint.sh 파일을 삭제합니다.
RUN rm -rf /usr/local/bin/docker-entrypoint.sh
# 공통적으로 적용할 redis.conf 파일을 복사합니다.

# Container가 생성, 시작하는 시점에 실행 시킬 docker-entrypoint.sh 파일을 복사합니다.
COPY 5.0.4/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

## change access authority
#RUN chmod 755 /usr/local/bin/redis.conf
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh

#RUN chown redis:redis /usr/local/bin/redis.conf
RUN chown redis:redis /usr/local/bin/docker-entrypoint.sh

#Redis Container에 대한 Port를 지정합니다. (내부포트이며 외부노출은 안됨)
#CLIENTPORT에 대한 값은 docker-compose.yml에 정의되어 있습니다.
EXPOSE $CLIENTPORT

# Container가 생성, 시작하는 시점에 실행됩니다.
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
# Container 빌드가 완료되고 Redis Server를 실행시킵니다.
CMD [ "redis-server","/usr/local/bin/conf/redis.conf" ]