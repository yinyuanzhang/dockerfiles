ARG VERSION=2.24.1

##### Get the built cache as a seperate layer as dockerhub caching does not work well with this method of versioning
FROM bauk/git:centos-build-${VERSION} as build

##### Final small image, just copying everything needed from build image
FROM bauk/git:centos-base
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
WORKDIR /git

COPY --from=build /usr/local /usr/local
COPY --from=build /build/git/contrib/completion/git-completion.bash /etc/bash_completion.d/

# Set up gitconfig files as entrypoint.sh won't do this if --user is specified
RUN git config --system include.path "/.gitconfig" \
 && git config --system --add include.path "/gitconfig" \
 && git config --system --add include.path "/.generated/gitconfig" \
 && mkdir /.generated \
 && chmod 777 /.generated

# To install git-repo-filter
#RUN yum install -y python3 wget
#RUN wget -O /bin/git-filter-repo https://raw.githubusercontent.com/newren/git-filter-repo/master/git-filter-repo \
# && chmod +x /bin/git-filter-repo \
# && wget -O /usr/share/man/man1/git-filter-repo.1 https://raw.githubusercontent.com/newren/git-filter-repo/docs/man1/git-filter-repo.1
