FROM python:3
MAINTAINER bagricola@squiz.co.uk

RUN pip install yamllint ansible-lint
# NOTE: Once https://github.com/willthames/ansible-review/pull/79 
# is merged and a release cut, we'll switch back to installing from pip.
RUN pip install -e git+https://github.com/benagricola/ansible-review.git@master#egg=ansible-review
