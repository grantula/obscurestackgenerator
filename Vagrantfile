# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "bento/centos-7.2"
  config.vm.boot_timeout = 300

  config.vm.network "private_network", ip: "192.168.127.51"

  config.vm.provider "virtualbox" do |v, override|
    v.memory = 4096
    v.customize ["modifyvm", :id, "--hwvirtex", "off"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    set -e

    yum -y update --exclude=kernel*

    yum -y install readline ca-certificates unzip epel-release

    # Add docker repo to yum
    tee /etc/yum.repos.d/docker.repo <<-'EOF'
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF

    # Install docker
    yum -y install docker-engine
    systemctl enable docker.service
    systemctl start docker
    usermod -aG docker vagrant

    chmod 777 /var/run/docker.sock
    sudo yum -y install nginx

    tee /etc/nginx/conf.d/obscurestackgenerator.conf <<'EOF' > /dev/null
server {
    listen 80;
    server_name obscurestackgenerator.dev;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
    }
}
EOF

    tee /etc/nginx/conf.d/api-obscurestackgenerator.conf <<'EOF' > /dev/null
server {
    listen 80;
    server_name api.obscurestackgenerator.dev;

    client_max_body_size 20M;

    location / {
        proxy_pass http://127.0.0.1:8081;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
    }
}
EOF

    systemctl enable nginx
    systemctl start nginx

    # Allow httpd to talk to ports
    sudo setsebool -P httpd_can_network_connect=true

    # Download and install docker-compose
    curl -s -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    chmod 755 /usr/local/bin/docker-compose

    # Install pip
    curl -O https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    rm -f get-pip.py

  SHELL

  config.vm.provision "recompose", type: "shell", run: "always", privileged: false, inline: <<-SHELL

    set -e

    cd /vagrant

    # Wait for the docker daemon to start up
    while [ ! -f /var/run/docker.pid ]; do sleep .5; done

    # Create a network for all containers to use if it doesn't already exist
    set +e
    docker network ls | grep 'docker_container_network'
    if [ ! $? == 0 ]; then docker network create docker_container_network; fi
    set -e

    # Clear old images
    /usr/local/bin/docker-compose -f consul-docker-compose.yml down

    # Pull latest images
    /usr/local/bin/docker-compose -f consul-docker-compose.yml pull

    # Start our docker containers
    /usr/local/bin/docker-compose -f consul-docker-compose.yml up -d

    # Give vault some time to start up
    sleep 8

  SHELL

end
