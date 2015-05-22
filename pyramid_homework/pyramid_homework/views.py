from pyramid.i18n import TranslationStringFactory


_ = TranslationStringFactory('pyramid_homework')


def index_view(request):
    return {'page_title': 'Index',
            'page_content':'Welcome you are in index.html',
            'link':'about/about.html',
            'link_label':'LINK TO aboutme.html'}

def about_view(request):
    return {'page_title': 'About me',
            'page_content':'Welcome you are in about.html',
            'link':'../index.html',
            'link_label':'LINK TO index.html'}

