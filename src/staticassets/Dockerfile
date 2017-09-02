FROM openresty/openresty:centos

# Install consul-template
ENV CONSUL_TEMPLATE_VERSION 0.18.1
RUN set -x \ 
    && yum -y install wget \
    && wget -O get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
    && python get-pip.py \
    && rm -f get-pip.py \
    && pip install dumb-init \
    && wget -O /tmp/consul-template.zip "https://releases.hashicorp.com/consul-template/$CONSUL_TEMPLATE_VERSION/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \
    && unzip -d /usr/local/bin /tmp/consul-template.zip \
    && rm /tmp/consul-template.zip \
    && chmod 755 /usr/local/bin/consul-template \
    && mkdir -p /etc/nginx/conf.d \
    && yum -y remove wget 

ENTRYPOINT ["dumb-init", "--"]
