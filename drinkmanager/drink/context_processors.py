from django.conf import settings

def squelette(request):
    completeurl = request.build_absolute_uri()
    basehost = request.get_host()
    basescheme = request.scheme
    baseurl = "%s://%s" % (basescheme,basehost)
    qrdroidurl = 'https://play.google.com/store/apps/details?id=me.scan.android.client&utm_source=global_co&utm_medium=prtnr&utm_content=Mar2515&utm_campaign=PartBadge&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'
    qrreaderurl = 'https://geo.itunes.apple.com/us/app/qr-reader-for-iphone/id368494609?mt=8'
    context = {
        'baseurl': baseurl,
        'basehost': basehost,
        'completeurl': completeurl,
		'qrdroidurl': qrdroidurl, 
		'qrreaderurl': qrreaderurl,
    }
    return context
