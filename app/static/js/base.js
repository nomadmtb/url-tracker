// Hide and fade in the element (ele).
function toggle_element(ele) {
  ele.hide().delay(500).fadeIn();
}

// Process the click table data.
function process_click_chart(ele) {

  var url = ele.attr('key');
  console.log(url);
  console.log(ele);

  var jqxhr = $.getJSON(url, function() {
    console.log("Success!");
  })
  .done( function(data) {

    var chart_labels = [];
    var chart_data = [];

    for (var key in data) {
      chart_labels.push(key);
      chart_data.push(data[key]);
    }

    var myLineChart = new Chart(ele, {
      type: 'line',
      data: {

        labels: chart_labels,
        datasets: [{
          label: 'Number of clicks',
          data: chart_data,
          backgroundColor:
            'rgba(66, 139, 202, 0.75)',
          borderColor:
            'rgba(66, 139, 202, 0.75)',
          hoverBackgroundColor:
            'rgba(66, 139, 202, 0.75)',
          borderWidth: 1,
        }]
      },

      options: {
        scales: {
          yAxes: [{
            ticks: {
              min: 0,
              stepSize: 10,
            }
          }]
        }
      }
    });

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
  if ( $('#click_chart').length ) {
    console.log('detected table.')
    process_click_chart( $('#click_chart') );
  }

  //...

});
