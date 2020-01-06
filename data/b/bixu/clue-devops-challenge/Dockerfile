FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y curl \
    && curl --silent https://raw.githubusercontent.com/habitat-sh/habitat/master/components/hab/install.sh | bash \
    && useradd --system hab \
    && hab pkg install 'core/hab-sup' \
    && hab pkg install 'core/hab-launcher' \
    && hab pkg install 'bixu/clue-devops-challenge' --channel=unstable

ENTRYPOINT ["/bin/hab", "sup", "run", "bixu/clue-devops-challenge", "--channel=unstable", "--strategy=at-once"]
