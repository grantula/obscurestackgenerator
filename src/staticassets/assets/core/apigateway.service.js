/*
 * Filename: assets/global/js/apigateway.js
 * Author(s): Grant W
 *
 * All requests to the api are funneled through this service.
 */

(function() {
    angular
        .module('app.core')
        .factory('ApiGatewayService', ApiGatewayService);

    ApiGatewayService.$inject = ['$http',
                                 '$q',
                                 'config',
                                 '$log',
                                 'CoreService'];

    function ApiGatewayService($http, $q, config, $log, CoreService) {

        var apiDomain = config.apiUrl;

        var service = {
            get: get,
            post: post,
            put: put,
            delete: delete_
        };

        return service;

        //////////////////////

        function handleResponse(response) {
            $log.debug(response);
            return response.data;
        }

        function handleError(response) {
            $log.error('Error making http call:');
            $log.error(response);

            var message;
            if (response.data !== null
                    && response.data.message !== undefined) {
                message = response.data.message;
            } else if (response.data !== null) {
                message = response.data;
            } else if (response.status !== 0) {
                message = "The API returned a status code of "
                          + response.status + " (" + response.statusText
                          + ")";
            } else {
                message = "The request to the API failed. Please check the "
                          + "javascript console for more information.";
            }

            return $q.reject(response.status + " : " + message);
        }

        function get(endpoint, headers, otherOptions) {
            otherOptions = otherOptions || {};

            var url = apiDomain + endpoint;

            $log.debug('GET: ' + url);
            $log.debug(otherOptions);

            return $http.get(url, otherOptions)
                        .then(handleResponse, handleError);
        }

        function post(endpoint, data, headers, otherOptions) {
            otherOptions = otherOptions || {};

            var url = apiDomain + endpoint;

            $log.debug('POST: ' + url);
            $log.debug(data);
            $log.debug(otherOptions);

            return $http.post(url, data, otherOptions)
                        .then(handleResponse, handleError);
        }

        function put(endpoint, data, headers, otherOptions) {
            otherOptions = otherOptions || {};

            var url = apiDomain + endpoint;

            $log.debug('PUT: ' + url);
            $log.debug(data);
            $log.debug(otherOptions);

            return $http.put(url, data, otherOptions)
                        .then(handleResponse, handleError);
        }

        function delete_(endpoint, headers, otherOptions) {
            otherOptions = otherOptions || {};

            var url = apiDomain + endpoint;

            $log.debug('DELETE: ' + url);
            $log.debug(otherOptions);

            return $http.delete(url, otherOptions)
                        .then(handleResponse, handleError);
        }
    }
})()
