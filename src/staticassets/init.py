import os
import subprocess

## Using system python which is 2.7.5

print "Starting init"

process = subprocess.Popen([
        '/usr/local/bin/consul-template',
            '-consul-addr', os.environ['CONSUL_ADDRESS'],
            '-config', '/usr/src/staticassets/consul-template.hcl'
        ])
print process.__dict__
process.wait()
