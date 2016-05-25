
def boston(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, TAX, RAD, PTRATIO, B, LSTAT, MEDV):
    HTML_text2 = "<p>CRIM = %s" % CRIM
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

    HTML_text1 = "<p>MEDV = %s" % MEDV

    result_dict = {
            'HTML_text2': HTML_text2,
            'HTML_text1': HTML_text1,
               }


    return result_dict
