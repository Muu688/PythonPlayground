import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()


graph = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Analysis of course reviews'
    },
    subtitle: {
        text: 'Average Rating by Day'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

# The main webpage
def app():
    wp = jp.QuasarPage()

    # Write elements for the Wep Page
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-body1")
    hc = jp.HighCharts(a=wp, options=graph)
    
    x = [3, 6 ,8]
    y = [4, 7, 9]
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])
    return wp

jp.justpy(app)