// Hide and fade in the element (ele)
function toggle_element(ele) {
  ele.hide().delay(500).fadeIn();
}

// Document READY.
$(document).ready(function(){
  console.log('Ready!');

  // Look for that create form and fade it in.
  if ( $('#create-container').length ) {
    toggle_element( $('#create-container') );
  }

  //...

});
