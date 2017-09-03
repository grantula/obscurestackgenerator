FROM python:3.6.2-slim

# INSTALL ENVCONSUL, ADD USER ACCOUNT
ENV ENVCONSUL_VERSION 0.6.1
RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates wget unzip openssl && update-ca-certificates \
    && wget -O /tmp/envconsul.zip "https://releases.hashicorp.com/envconsul/$ENVCONSUL_VERSION/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip" \
    && unzip -d /bin /tmp/envconsul.zip && rm /tmp/envconsul.zip && chmod 755 /bin/envconsul \
    && apt-get purge -y wget unzip \
    && rm -rf /var/lib/apt/lists/* \
    && addgroup --system sysuser \
    && adduser --system -shell /sbin/nologin sysuser \
    && adduser sysuser sysuser

# Install system packages needed by this container and create directory for code
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc6-dev \
    && mkdir -p /usr/src \
    && touch /usr/src/__init__.py \
    && pip install --no-cache-dir \
        dumb-init \
        flask==0.12 \
        nose==1.3.7 \
        psycopg2 \
        simplejson==3.8.1 \
        SQLAlchemy==1.0.11 \
        uwsgi==2.0.15 \
    && apt-get purge -y gcc gcc-4.9 cpp cpp-4.9 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/stackoptions-python
COPY src/stackoptions-python/envconsul.hcl /etc/

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
