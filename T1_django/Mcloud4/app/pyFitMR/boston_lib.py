
def boston(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, TAX, RAD, PTRATIO, B, LSTAT):
    from django.conf import settings
    import os
    import numpy
    from sklearn.externals import joblib

    if CRIM and ZN and INDUS and CHAS and NOX and RM and AGE and DIS and TAX and RAD and PTRATIO and B and LSTAT:
        demo_data = 0
    else: #default value for testing
        CRIM=1.6566
        ZN=0.
        INDUS=19.58
        CHAS=0.
        NOX=0.871
        RM=6.122
        AGE=97.3
        DIS=1.618
        TAX=5.
        RAD=403.
        PTRATIO=14.7
        B=372.8
        LSTAT=14.1
        demo_data = 1

    X = numpy.array([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, TAX, RAD, PTRATIO, B, LSTAT], dtype = numpy.float64)
    lr = joblib.load(os.path.join(settings.PROJECT_ROOT, 'app', 'lrmachine.pkl'))
    MEDV = lr.predict(X)

    HTML_text2 =' <h4>Input data</h4>'
    HTML_text2 += "<p>CRIM = %s" % CRIM
    HTML_text2 += "<p>ZN = %s" % ZN
    HTML_text2 += "<p>INDUS = %s" % INDUS
    HTML_text2 += "<p>CHAS = %s" % CHAS
    HTML_text2 += "<p>NOX = %s" % NOX
    HTML_text2 += "<p>RM = %s" % RM
    HTML_text2 += "<p>AGE = %s" % AGE
    HTML_text2 += "<p>DIS = %s" % DIS
    HTML_text2 += "<p>TAX = %s" % TAX
    HTML_text2 += "<p>RAD = %s" % RAD
    HTML_text2 += "<p>PTRATIO = %s" % PTRATIO
    HTML_text2 += "<p>B = %s" % B
    HTML_text2 += "<p>LSTAT = %s" % LSTAT

    HTML_text1 =' <h4>Prediction of the real estate in Boston</h4>'
    HTML_text1 += "<h3> %s </h3>" % MEDV

    import Plotting_lib
    from sklearn.cross_validation import cross_val_predict

    chart_title = 'Boston real estate forecast'
    xAxis_label = 'Measured'
    yAxis_label = 'Predicted'

    result_dict = {
            'HTML_text1': HTML_text1,
            'HTML_text2': HTML_text2,
            'SVG':Plotting_lib.dynamic_svg1(MEDV, xAxis_label, yAxis_label),
            'highchart':Plotting_lib.highchart1(MEDV, xAxis_label, yAxis_label, chart_title)
               }
    return result_dict
