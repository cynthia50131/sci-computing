def dynamic_svg(x,y,smoothx, smoothy,xAxis_label,yAxis_label,chart_title):
    import StringIO
    import numpy, matplotlib.pyplot as plt
    #import seaborn as sns
    try:
        #sns.set_style('ticks')
        #plt.style.use('ggplot')
        #plt.title('T1 fitting for Look-Locker Experiment')
        #plt.scatter(x,y, s=65, color=sns.color_palette()[0],marker='o',alpha=0.8)
        #plt.plot(smoothx, fitted_y, color=sns.color_palette()[1])
        plt.figure(1)
        plt.clf()
        #pylab.rcParams.update(params)
        plt.scatter(x,y, s=65, marker='+',c= 'k',label='Original')
        plt.plot(smoothx, smoothy,c= 'k',label='Fitted data')
        plt.legend(loc='lower right')
        plt.xlabel(xAxis_label)
        plt.ylabel(yAxis_label)
        plt.xlim(xmin =-10,xmax= max(x)+100)
        plt.ylim(ymin =smoothy.min()-10)
        fig = plt.gcf()
        fig.set_size_inches(10,6)
        #plt.gca().axhline(0, color='black', lw=2)
        plt.gca().grid(True)

        #plt.gca().set_axis_bgcolor('white')
        rv = StringIO.StringIO()
        plt.savefig(rv, format="svg")
        return rv.getvalue()
    finally:
        plt.clf()


def dynamic_svg1(MEDV, xAxis_label, yAxis_label):
    import StringIO
    import numpy, matplotlib.pyplot as plt


    from sklearn import datasets
    from sklearn.cross_validation import cross_val_predict
    from sklearn import linear_model
    import matplotlib.pyplot as plt

    lr = linear_model.LinearRegression()
    boston = datasets.load_boston()
    y = boston.target

    try:
        plt.figure(1)
        plt.clf()
        #plt.scatter(x,y, s=65, marker='+',c= 'k',label='Original')
        #plt.plot(smoothx, smoothy,c= 'k',label='Fitted data')
        #plt.legend(loc='lower right')

        predicted = cross_val_predict(lr, boston.data, y, cv=10)

        fig, ax = plt.subplots()
        plt.scatter(predicted, y, s=4, color = '0')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], 'b--', lw=2)
        plt.plot(MEDV, MEDV, 'r*', markersize=15)
        plt.xlabel(xAxis_label)
        plt.ylabel(yAxis_label)
        #plt.xlabel('Measured')
        #plt.ylabel('Predicted')
        #plt.set_xlabel('Measured')
        #plt.set_ylabel('Predicted')
        #plt.xlim(xmin =-10,xmax= max(x)+100)
        #plt.ylim(ymin =smoothy.min()-10)
        fig = plt.gcf()
        fig.set_size_inches(10,6)
        plt.gca().grid(True)
        rv = StringIO.StringIO()
        plt.savefig(rv, format="svg")
        return rv.getvalue()
    finally:
        plt.clf()


def highchart(x,y,smoothx, fitted_y,xAxis_label,yAxis_label,chart_title):
    original_data = ''
    for index in range(len(x)):
            if (index < (len(x) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (x[index], y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (x[index], y[index])
            original_data +=formattedline


    fitted_data = ''
    for index in range(len(fitted_y)):
            if (index < (len(fitted_y) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (smoothx[index], fitted_y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (smoothx[index], fitted_y[index])
            fitted_data += formattedline

    JS="""
                <script type='text/javascript'>
                $(function () {
                    $('#container2').highcharts({

                            credits: {
                    text: '',
                    href: 'http://cloud.mrilab.org'
                },
                        chart: {
                            type: 'scatter',
                            zoomType: 'xy'
                        },
                        title: {
                            text: '""" +  chart_title + """'
                        },

                        xAxis: {
                            title: {
                                enabled: true,
                                text: '""" +  xAxis_label + """'
                            },
                            startOnTick: true,
                            endOnTick: true,
                            showLastLabel: true
                        },
                        yAxis: {
                            title: {
                                text: '""" +  yAxis_label + """'
                            }
                        },
                        legend: {
                            layout: 'vertical',
                            align: 'left',
                            verticalAlign: 'top',
                            x: 100,
                            y: 70,
                            floating: true,
                            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
                            borderWidth: 1
                        },
                        plotOptions: {
                            scatter: {
                                marker: {
                                    radius: 5,
                                    states: {
                                        hover: {
                                            enabled: true,
                                            lineColor: 'rgb(100,100,100)'
                                        }
                                    }
                                },
                                states: {
                                    hover: {
                                        marker: {
                                            enabled: false
                                        }
                                    }
                                },
                                tooltip: {
                                    headerFormat: '<b>{series.name}</b><br>',
                                    pointFormat: '{point.x} ms, {point.y} '
                                }
                            }
                        },
                        series: [{
                            name: 'Original',
                            color: 'rgba(223, 83, 83, .8)',

                            data: [	""" +  original_data + """	]

                        }, {
                            name: 'Fitted Data',
        			        lineWidth: 3,
        			         marker: {
                                            enabled: false
                                        },
                            color: 'rgba(119, 152, 191, 1)',
                            data: [	""" +  fitted_data + """	]
                        }]
                    });
                });


        </script>


        <div id='container2' style='width: 80%; height: 480px; margin: 0 auto;'></div>


        """
    return JS


def highchart1(MEDV, xAxis_label, yAxis_label, chart_title):
    from sklearn import datasets
    from sklearn.cross_validation import cross_val_predict
    from sklearn import linear_model
    import matplotlib.pyplot as plt

    lr = linear_model.LinearRegression()
    boston = datasets.load_boston()
    y = boston.target
    predicted = cross_val_predict(lr, boston.data, y, cv=10)

    original_data = ''

    for index in range(len(y)):
            if (index < (len(y) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (predicted[index], y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (predicted[index], y[index])
            original_data += formattedline


    fitted_data = ''
    for index in range(len([y.min(), y.max()])):
            if (index < (len([y.min(), y.max()]) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % ([y.min(), y.max()][index], [y.min(), y.max()][index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % ([y.min(), y.max()][index], [y.min(), y.max()][index])
            fitted_data += formattedline

    final = ''

    for index in range(len(MEDV)):
            if (index < (len(MEDV) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (MEDV[index], MEDV[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (MEDV[index], MEDV[index])
            final += formattedline

    JS="""
                <script type='text/javascript'>
                $(function () {
                    $('#container2').highcharts({

                            credits: {
                    text: '',
                    href: 'http://cloud.mrilab.org'
                },
                        chart: {
                            type: 'scatter',
                            zoomType: 'xy'
                        },
                        title: {
                            text: '""" +  chart_title + """'
                        },

                        xAxis: {
                            title: {
                                enabled: true,
                                text: '""" +  xAxis_label + """'
                            },
                            startOnTick: true,
                            endOnTick: true,
                            showLastLabel: true
                        },
                        yAxis: {
                            title: {
                                text: '""" +  yAxis_label + """'
                            }
                        },
                        legend: {
                            layout: 'vertical',
                            align: 'left',
                            verticalAlign: 'top',
                            x: 100,
                            y: 70,
                            floating: true,
                            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
                            borderWidth: 1
                        },
                        plotOptions: {
                            scatter: {
                                marker: {
                                    radius: 5,
                                    states: {
                                        hover: {
                                            enabled: true,
                                            lineColor: 'rgb(100,100,100)'
                                        }
                                    }
                                },
                                states: {
                                    hover: {
                                        marker: {
                                            enabled: false
                                        }
                                    }
                                },
                                tooltip: {
                                    headerFormat: '<b>{series.name}</b><br>',
                                    pointFormat: '{point.x} ms, {point.y} '
                                }
                            }
                        },
                        series: [{
                            name: 'Boston data',
                            marker: {
                                    radius: 4
                                            },
                            color: 'rgba(167, 167, 211, .8)',
                            data: [	""" +  original_data + """	]

                        }, {
                            name: 'Standard line',
        			        lineWidth: 3,
        			         marker: {
                                            enabled: false
                                        },
                            color: 'rgba(147, 147, 72, 1)',
                            data: [	""" +  fitted_data + """	]
                        }, {
                            name: 'Predicte Price',
                            marker: {
                                    radius: 6
                                            },

                            color: 'rgba(174, 91, 91, .8)',
                            data: [	""" +  final + """	]

                        }]
                    });
                });


        </script>


        <div id='container2' style='width: 80%; height: 550px; margin: 0 auto;'></div>


        """
    return JS
