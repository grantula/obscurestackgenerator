import os
import subprocess

## Using system python which is 2.7.5

print "Starting init"

process = subprocess.Popen([
        '/usr/local/bin/consul-template',
            '-consul-addr', os.environ['CONSUL_ADDRESS'],
            '-config', '/usr/src/webgateway/consul-template.hcl'
        ])

process.wait()
