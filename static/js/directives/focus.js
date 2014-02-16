app.directive('toFocus', function ($timeout) {
    return function (scope, elem, attrs) {
        scope.$watch(attrs.toFocus, function (newval) {
            if (newval) {
                $timeout(function () {
                    elem[0].focus();
                }, 0, false);
            }
        });
    };
});
