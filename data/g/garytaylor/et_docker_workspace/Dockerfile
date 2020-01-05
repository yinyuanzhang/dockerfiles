FROM garytaylor/ruby_docker_workspace:0.1.0
ENV DEBIAN_FRONTEND noninteractive
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y pdftk nodejs postgresql-client-9.6 libpq5 libpq-dev
