
(function () {
  
  function setup() {
    var SCROLL_TIMEOUT;

    // Whether we're animating.
    var ANIMATING = false;
    
    // Whether the user is currently touching the screen.
    var TOUCHING = false;
    
    // Flag for whether we should snap the scroll when the user lifts her
    // finger.
    var ADJUST_ON_TOUCH_END = false;

    var $catList = $('.category-list');
    var $categories = $('.category-list .category');

    $catList.on('touchstart', function () {
      TOUCHING = true;
    });
    
    $catList.on('touchend', function () {
      if (ADJUST_ON_TOUCH_END) {
        schedule();
        ADJUST_ON_TOUCH_END = false;
      }
      TOUCHING = false;
    });
    $catList.on('scroll', function (event) {
      if (ANIMATING) {
        // Don't allow any scrolling during the animation because it will
        // look weird as hell.
        event.preventDefault();
      }
      if (TOUCHING) {
        ADJUST_ON_TOUCH_END = true;
        return;
      }
      
      schedule();
    });
    
    function schedule() {
      if (SCROLL_TIMEOUT) {
        clearTimeout(SCROLL_TIMEOUT);
        SCROLL_TIMEOUT = null;
      }
      SCROLL_TIMEOUT = setTimeout(snapScroll, 400);
    }
    
    function snapScroll() {
      var currentLeft = $catList[0].scrollLeft;

      // Grab the current left-offsets of the category container elements.
      // The first element will always be 0, so if we get (e.g.) 10 for the
      // first element, assume everything is off by 10.
      var offsets = $.map($categories, function(node) {
        return node.offsetLeft - $categories[0].offsetLeft;
      });

      // Keep track of which offset is the closest one to where we are.
      var closest;
      var lowestDelta;
      
      offsets.forEach(function (offset) {
        var delta = Math.abs(currentLeft - offset);
        if (typeof closest !== 'number' || delta < lowestDelta) {
          lowestDelta = delta;
          closest = offset;
        }
      });
      
      ANIMATING = true;
      $catList.animate({
        scrollLeft: closest
      }, 200).promise().done(function () {
        ANIMATING = false;
      });
    }
  }
  
  $(setup);
})();


