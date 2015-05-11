def clean_value(type, val):
    retval = val
    if retval == 'N/A' or retval == '':
        return None
    retval = retval.replace(',','')
    retval = retval.upper()
    if retval.endswith('B'):
        retval = retval.replace('B','')+'000000000'
    elif retval.endswith('M'):
        retval = retval.replace('M','')+'000000'
    return type(retval)