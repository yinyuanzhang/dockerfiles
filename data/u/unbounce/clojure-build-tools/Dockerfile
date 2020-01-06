FROM library/clojure:lein-2.8.1
MAINTAINER Raymond Huang <raymond.huang@unbounce.com>
LABEL Description="This image is used for packaging Clojure Projects on Jenkins."

RUN apt-get update

# install make
RUN apt-get install -y make

# This is needed to run on Jenkins because  (b/c they're tied to user ids)
RUN useradd --uid 1002 --create-home jenkins-user-1002
RUN useradd --uid 1001 --create-home jenkins-user-1001

# This allows *any* user to run lein otherwise it will fail complaining about
# trying to create a .lein folder
RUN mkdir /.lein

# Cache build artifacts inside repo to speedup Jenkins build speed
# See https://github.com/technomancy/leiningen/blob/master/doc/PROFILES.md#declaring-profiles
COPY profiles.clj /etc/leiningen/profiles.clj
