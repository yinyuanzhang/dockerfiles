FROM alpine:latest
RUN apk add --no-cache curl

FROM redmine:latest

WORKDIR /usr/src/redmine/plugins

# Recurring Tasks https://www.redmine.org/plugins/redmine_recurring_tasks
RUN git clone --depth 1 https://github.com/centosadmin/redmine_recurring_tasks.git

WORKDIR /usr/src/redmine

