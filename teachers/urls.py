
def qs2html(qs):
    lst= []
    if qs is not None:
        for i in qs:
            lst.append(str(i))
    else:
        'QuerySet is empty'
    return '<br>'.join(lst)

