
@view_config(route_name='index', renderer='index.html')
def index(request):
    sections = [
        {'name': 'home', 'icon': 'home'},
        {'name': 'news', 'icon': 'announcement'},
        {'name': 'about', 'icon': 'book'},
        {'name': 'documents', 'icon': 'file text outline'},
        {'name': 'contact', 'icon': 'mail'},
        {'name': 'auth', 'icon': 'sign in'},
    ]
    return {'sections': sections}

