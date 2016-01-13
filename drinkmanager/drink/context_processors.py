from django.conf import settings

def squelette(request):
    completeurl = request.build_absolute_uri()
    basehost = request.get_host()
    basescheme = request.scheme
    baseurl = "%s://%s" % (basescheme,basehost)
    context = {
        'baseurl': baseurl,
        'basehost': basehost,
        'completeurl': completeurl,
    }
    return context
