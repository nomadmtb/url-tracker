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
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255,99,132,1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
        }]
      },

      options: {}
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
