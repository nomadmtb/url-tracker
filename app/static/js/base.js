// Hide and fade in the element (ele).
function toggle_element(ele) {
  ele.hide().delay(500).fadeIn();
}

// Process the click table data.
function process_click_table(ele) {
  ele.hide();
  $.getJSON(ele.attr('key'), function( data ) {

    ele.fadeIn();

  });
}

// Document READY.
$(document).ready(function(){
  console.log('Ready!');

  // Look for that create form and fade it in.
  if ( $('#create-container').length ) {
    toggle_element( $('#create-container') );
  }

  // Look for the click data table.
  if ( $('#click_table').length ) {
    process_click_table( $('#click_table') );
  }

  //...

});
