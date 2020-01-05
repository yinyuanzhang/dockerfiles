FROM plexinc/pms-docker:latest

RUN apt-get update && apt-get install -y \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY --from=tellytv/telly:dev /app /opt/tellytv
ADD run-tellytv.sh /etc/services.d/tellytv/run
