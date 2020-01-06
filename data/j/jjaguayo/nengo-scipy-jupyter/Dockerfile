FROM jupyter/scipy-notebook
RUN pip install nengo==2.3.1

# A defect in the version 2.3.1 and this version of ensemble.py is simply to
# patch. This copy can be removed when a new version of nengo fixes this issue.

COPY ensemble.py /opt/conda/lib/python3.5/site-packages/nengo/ensemble.py
