google.charts.load('current', {
      'packages': ['gantt']
    });
    google.charts.setOnLoadCallback(drawChart);

    function daysToMilliseconds(days) {
      return days * 24 * 60 * 60 * 1000;
    }

    function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Task ID');
      data.addColumn('string', 'Task Name');
      data.addColumn('date', 'Start Date');
      data.addColumn('date', 'End Date');
      data.addColumn('number', 'Duration');
      data.addColumn('number', 'Percent Complete');
      data.addColumn('string', 'Dependencies');

      data.addRows([
        ['P1', 'Initiation', new Date(2022, 0, 10), new Date(2022, 0, 17), null, 100, null],
        ['P2', 'Planning', new Date(2022, 0, 20), new Date(2022, 0, 27), null, 75, 'P1'],
        ['P3', 'Execution', new Date(2022, 1, 7), new Date(2022, 1, 14), null, 50, 'P2'],
        ['P4', 'Evaluation', new Date(2022, 1, 17), new Date(2022, 1, 20), null, 25, 'P3'],
        ['P5', 'Closing', new Date(2022, 1, 22), new Date(2022, 1, 23), null, 0, 'P4']
      ]);

      var options = {
        height: 275,
         gantt: {
          criticalPathEnabled: true,
          innerGridHorizLine: {
            stroke: '#ffe0b2',
            strokeWidth: 2
          },
          innerGridTrack: {fill: '#fff3e0'},
          innerGridDarkTrack: {fill: '#ffcc80'}
        }
     
      };

      var chart = new google.visualization.Gantt(document.getElementById('chart_div'));

      chart.draw(data, options);
    }
