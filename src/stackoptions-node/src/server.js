'use strict';

const express = require('express');

// Constants
const PORT = 80;
const HOST = '0.0.0.0';

// App
const app = express();

app.get('/v1/stack_options', (req, res) => {
    res.send({
        operatingSystem: [
            'ubuntu',
            'centos',
            'debian',
            'freebsd',
            'openbsd',
            'suse',
            'fedora'
        ],
        backEnd: [
            'python',
            'node',
            'java',
            'c#',
            'ruby',
            'go',
            'erlang',
            '.net'
        ],
        frontEnd: [
            'react',
            'angular1',
            'angular2',
            'angular4',
            'emberjs',
            'vanilla javascript',
            'vuejs',
            'backbone'
        ],
        server: [
            'apache',
            'nginx',
            'mongoose'
        ]
    });
});

app.get('/status', (req, res) => {
    console.info(req.headers);
    res.send('Ok!');
});

app.listen(PORT, HOST);
