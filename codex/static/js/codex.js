var travelersCodexApp = angular.module('travelersCodexApp', []);

travelersCodexApp.controller('ItemCtrl', function($scope) {
    // TODO: Actually fetch items via Ajax/search.

    $scope.items = [
       { name: 'Sapphire Wire', 
          description: 'A favorite of Hunters because of its versatility, this wire is incorporated into almost all Hunter gear.',
          image: '/static/img/item_icons/sapphire_wire.png'
      },
        { name: 'Spinmetal', 
          description: 'A filigree of bubbled metal grown by wild colonies of Golden Age cytoconstructors.',
          image: '/static/img/item_icons/spinmetal.png'
      }
    ];
});

