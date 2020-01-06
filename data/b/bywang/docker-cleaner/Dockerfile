FROM docker
ENV CLEAN_INTERVAL=3600
ENV CLEAN_FILTER="until=48h"
WORKDIR /app
COPY . .
CMD ["sh", "./clean_docker.sh"]
