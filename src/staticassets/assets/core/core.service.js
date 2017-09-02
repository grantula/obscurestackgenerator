/*
 * Filename: assets/core/apigateway.js
 * Author(s): Grant W
 *
 * All requests to the api are funneled through this service.
 */

(function() {
    angular
        .module('app.core')
        .factory('CoreService', CoreService);

    CoreService.$inject = ['$http', '$q', 'config'];

    function CoreService($http, $q, config) {

        var service = {
            objToQueryStr: objToQueryStr,
            queryStrToObj: queryStrToObj,
            toTitleCase: toTitleCase,
            randomSelection: randomSelection,
            toSet: toSet
        };
        return service;

        //////////////////////

        function objToQueryStr(obj) {

            if (angular.equals(obj, {})) return '';

            var params = [];

            // Order is not preserved, will want to build string
            // manually when order is necessary
            for (var key in obj) {
                params.push(key + '=' + obj[key]);
            }

            return '?'+params.join('&');
        }

        function queryStrToObj(queryStr) {
             //pass to this function $window.location.search
             if (angular.equals(queryStr, '')) return {};

            var pairs = queryStr.slice(1).split('&');

            var result = {};
            pairs.forEach(function(pair) {
                pair = pair.split('=');
                result[pair[0]] = decodeURIComponent(pair[1] || '');
            });
            return JSON.parse(JSON.stringify(result));
        }

        function toTitleCase(stringText) {
            return stringText.split(' ').map(function(val){
                return val.charAt(0).toUpperCase() + val.substr(1).toLowerCase();
            }).join(' ');
        }

        function randomSelection(arr){
            return arr[Math.floor(Math.random() * arr.length)]
        }

        function toSet(arr) {
            /* similar to pythons set() method to remove duplicates from
            an array
            */
            var uniq = new Set();
            arr.forEach(e => uniq.add(JSON.stringify(e)));
            return Array.from(uniq).map(e => JSON.parse(e));
        }
    }
})()
