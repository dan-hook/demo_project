"""
Views.
"""

from django.shortcuts import render

BASE_PAIRING = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}

def home(request):
    context = {}

    # Check whether this request includes a query string to translate.
    query_string = request.GET.get('query', None)
    error = False
    if query_string:
        query_string = query_string.upper()
        reverse_complement = ''
        for base in query_string:
            try:
                reverse_complement += BASE_PAIRING[base]
            except KeyError:
                 error = True
                 break
        context['query_string'] = query_string
        if error:
           highlighted_errors = '<span>\n'
           for base in query_string:
             if base not in BASE_PAIRING.keys():
                 highlighted_errors += '<span style="color: red;font-weight:bold">' + base +'</span>'
             else:
                 highlighted_errors += base
           highlighted_errors += '</span>'
           context['bad_bases'] = highlighted_errors
        else: 
            context['reverse_complement'] = reverse_complement

    return render(request, 'home.html', context)
