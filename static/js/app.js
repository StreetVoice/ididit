'use strict';

var app = angular.module('app', ['djangoRESTResources', 'ngRoute', 'ngCookies']);

app.run(function($rootScope, $http, $cookies){
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
});


app.config(function($routeProvider, $locationProvider) {
  $routeProvider
      .when('/', {templateUrl: '/static/js/dashboard.html', controller: 'DoneController'})
      .when('/date/:date', {templateUrl: '/static/js/dashboard.html', controller: 'DoneController'})
      .when('/404', {templateUrl: '/static/js/404.html', controller: 'NotFoundController'})
      .otherwise({redirectTo: '/'});
});


app.controller('NotFoundController', ['$scope', function($scope) {
    console.log('404');
}]);


app.controller('DoneController', ['$scope', '$routeParams', '$http', '$location', 'djResource', 
        function($scope, $routeParams, $http, $location, djResource){
    
    $scope.show_action = false;

    var User = djResource('/api/users/:id/', {id: '@id'}, {update: {method: 'PUT'}});
    var Item = djResource('/api/items/:id/', {id: '@id'}, {update: {method: 'PUT'}});
    var ItemLike = djResource('/api/item_likes/');
    var ItemComment = djResource('/api/item_comments/');

    if ($routeParams.date === undefined) {
        var the_date = new Date();
    } else {
        var the_date = moment($routeParams.date).toDate();
    }

    var prev_date = new Date(the_date).setDate(the_date.getDate() - 1);
    var next_date = new Date(the_date).setDate(the_date.getDate() + 1);

    $scope.commentInput = {};

    $scope.the_date = the_date;
    $scope.prev_date = prev_date
    $scope.next_date = next_date

    var date = moment(the_date).format('YYYY-MM-DD');

    // retrive data
    $http.get('/api/me/').success(function(me){
        $scope.me = me;

        // my items
        var items = Item.query({user: me.id, date: date}, function(data){
            $scope.me.items = data;
        });

        // other users
        User.query(function(users){
            Item.query({date: date}, function(items){
                users.forEach(function(user, index, array){
                    user.items = [];

                    // arrange items with user
                    items.forEach(function(item, index, array){
                        if (item.user == user.id) {
                            user.items.push(item);
                        }
                    });

                    // move me to first
                    if (user.id == me.id) {
                        users.splice(0, 0, users.splice(index, 1)[0]);
                    }
                });

                $scope.users = users;
            });
        });

    });
    $scope.hideCommentInput = function(item){
        $scope.commentInput[item.id] = "";
        item.isShowInputDialog = false;
    }
    $scope.showCommentInput = function(item){
        console.log(item);
        item.isShowInputDialog = true;
    }
    $scope.submitComment = function(item){
        console.log(item);
        var comment = new ItemComment({
            user: '/api/users/' + $scope.me.id + '/',
            item: '/api/items/' + item.id +'/',
            text: $scope.commentInput[item.id]
        });

        comment.$save(function(data) {
            data.user = $scope.me;
            item.comments.push(data);
            console.log(item);
        }, function(error) {
            console.log(error.data);
        });
    }
    //
    $scope.submit = function(){
        var item = new Item({text: $scope.text, date: date});

        item.$save(function(data) {
            $scope.users[0].items.push(data);
        }, function(error) {
            console.log(error.data);
        });

        $scope.text = '';
    };

    $scope.like = function(item) {
        var like = new ItemLike({
            user: '/api/users/' + $scope.me.id + '/', 
            item: '/api/items/' + item.id + '/'
        });

        like.$save(function(data) {
            item.likes.push($scope.me.username);
        }, function(error) {
            console.log(error.data);
        });
    }

    $scope.delete = function(item) {
        if (item.user !== $scope.me.id) {
            alert("Opps, it's not yours");
            return false;
        }

        item.$delete({id: item.id}, function(data){
            var index = $scope.users[0].items.indexOf(item);
            $scope.users[0].items.splice(index, 1);
            
        }, function(error){ 
            console.log(error);
        });
    }

}]);
