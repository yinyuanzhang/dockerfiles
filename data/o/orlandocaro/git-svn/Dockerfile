FROM alpine
RUN apk update && apk upgrade
RUN apk -U add git git-svn subversion curl bash findutils vim nano python3
RUN cd $(git --exec-path) \
    && curl --insecure --connect-timeout 3 --silent -O https://raw.githubusercontent.com/newren/git-filter-repo/master/git-filter-repo \
    && chmod 755 git-filter-repo
ENV PYTHONPATH=/usr/local/lib/python3
RUN mkdir $PYTHONPATH \
    && cd $PYTHONPATH \
    && ln -s $(git --exec-path)/git-filter-repo git_filter_repo.py
RUN cd /usr/local/bin \
    && curl --insecure --connect-timeout 3 --silent -O https://raw.githubusercontent.com/newren/git-filter-repo/master/contrib/filter-repo-demos/clean-ignore \
    && chmod 755 clean-ignore
ADD *.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/*.sh
RUN adduser -D -h /data gituser
USER gituser
WORKDIR /data
