# =====================================================================
# Celery Flower Docker Image
# --------------------------
#
# Build Image:
# ------------
#
#     >>> docker build -t illagrenan/flower .
#
#
# Run Image:
# ----------
#
#     >>> docker run --rm -it -p 5555:5555 illagrenan/flower
#
# =====================================================================
FROM python:3.6.3-alpine3.6
LABEL authors="Vašek Dohnal <vaclav.dohnal@gmail.com>"

# ---------------------------------------------------------------------
# 1. System Settings
# ---------------------------------------------------------------------
# Disable output buffering
ENV PYTHONUNBUFFERED 1
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1

# ---------------------------------------------------------------------
# 2. Requirements
# ---------------------------------------------------------------------
RUN pip install --isolated --no-input --compile --exists-action=a --disable-pip-version-check --use-wheel --no-cache-dir 'flower~=0.9.2'

# ---------------------------------------------------------------------
# 3. Define process
# ---------------------------------------------------------------------
EXPOSE 5555
CMD ["flower", "--address=0.0.0.0", "--port=5555", "--inspect", "--log-to-stderr", "--logging=debug"]
