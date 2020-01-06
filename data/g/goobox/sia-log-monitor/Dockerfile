#
# Copyright (C) 2018 Junpei Kawamoto
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
FROM fluent/fluentd:stable
LABEL maintainer="Junpei Kawamoto <kawamoto.junpei@gmail.com>"

ENV SIA_DIRECTORY /sia
RUN gem install fluent-plugin-record-modifier --no-document

ADD entrypoint.sh /bin
ADD conf/* /fluentd/etc/

USER root
CMD fluentd -c /fluentd/etc/fluent.conf -p /fluentd/plugins
