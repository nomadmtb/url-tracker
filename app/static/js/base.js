// Hide and fade in the element (ele).
function toggle_element(ele, time) {
  ele.css('visibility','visible').hide().delay(500).fadeIn();
}

// Load the tooltips on the page.
function load_tooltips() {
  $('[data-toggle="tooltip"]').tooltip()
}

// Calculate the step values for the config.
// Be sure to pass in the length of the data.
function calculate_step(input_length) {
  var zero_count = ( input_length.toString().length - 1 );
  var str_step = "1";

  for (i = 0; i < zero_count; i++) {
    str_step += "0";
  }

  return parseInt(str_step);
}

// Find the max value from the chart data.
function find_max(input_data) {
  var current_max = 0;

  for (i = 0; i < input_data.length; i++) {

    if (input_data[i] > current_max) {
      current_max = input_data[i];
    }

  }

  return current_max;
}

// Process the click table data.
function process_click_chart(ele) {

  var url = ele.attr('key');

  var jqxhr = $.getJSON(url, function() {
    console.log('successful get');
  })
  .done( function(data) {

    var chart_labels = [];
    var chart_data = [];

    for (var key in data) {
      chart_labels.push(key);
      chart_data.push(data[key]);
    }

    console.log(chart_data);

    var myLineChart = new Chart(ele, {
      type: 'line',
      data: {

        labels: chart_labels,
        datasets: [{
          label: 'Number of clicks',
          data: chart_data,
          backgroundColor:
            'rgba(66, 139, 202, 0.50)',
          borderColor:
            'rgba(66, 139, 202, 0.50)',
          hoverBackgroundColor:
            'rgba(66, 139, 202, 0.50)',
          borderWidth: 1,
        }]
      },

      options: {
        scales: {
          yAxes: [{
            ticks: {
              min: 0,
              stepSize: calculate_step( find_max(chart_data) ),
            }
          }]
        }
      }
    });

  });
}

// Document READY.
$(document).ready(function(){

  // Look for that create form and fade it in.
  if ( $('#create-container').length ) {
    toggle_element( $('#create-form-wrapper'), 500 );
  }

  // Load all of the tooltips.
  load_tooltips();

  // Look for the click data table.
  if ( $('#click_chart').length ) {
    toggle_element( $('#view-container'), 500 );
    process_click_chart( $('#click_chart') );
  }

});
