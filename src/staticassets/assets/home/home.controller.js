/*
 * Filename: /static/home/home.controller
 * Author(s): Grant W
 *
 * This is the controller for the home page
 */

(function() {
    angular.module('app.home')
           .controller('HomeController', HomeController);

    HomeController.$inject = ['$scope', 'CoreService'];

    function HomeController($scope, CoreService) {

        var vm = this;

        vm.operatingSystem;
        vm.backEnd;
        vm.frontEnd;
        vm.dataBase;
        vm.server;
        vm.randomStack;
        vm.generateRandomStack = generateRandomStack;

        init();

        //////////////////////

        function init() {
            // These will eventually be db calls duh
            vm.operatingSystem = [
                'ubuntu',
                'centos',
                'debian',
                'freebsd',
                'openbsd',
                'suse',
                'fedora'
            ]

            vm.database = [
                'postgres',
                'sql server',
                'oracle',
                'sqlite',
                'mongodb',
                'couchdb',
                'dynamodb',
                'redis',
                'berkleydb',
                'memcache'
            ]

            vm.backEnd = [
                'python',
                'node',
                'java',
                'c#',
                'ruby',
                'go',
                'erlang',
                '.net'
            ]

            vm.frontEnd = [
                'react',
                'angular1',
                'angular2',
                'angular4',
                'vanilla javascript',
                'vuejs',
                'backbone'
            ]

            vm.server = [
                'apache',
                'nginx',
                'mongoose'
            ]
        }

        function generateRandomStack() {
            var toDo = ['backEnd', 'frontEnd', 'server', 'operatingSystem',
                        'database'];
            var selections = {};
            for (var t in toDo) {
                var current = toDo[t];
                var selection = CoreService.randomSelection(vm[current]);
                selections[current] = selection;
            }
            vm.randomStack = selections;
            return selections;
        }


    }
})()
