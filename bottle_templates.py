import os
from bottle import run, route, error, static_file, template

####################
#listi fyrir fréttir
####################
frettir = [
    {
        'heading': 'Frétt 1',
        'content': 'Donec metus eros, congue eu urna sit amet, dapibus luctus elit. Ut a risus vel leo hendrerit commodo. Fusce mattis tristique rutrum. Proin in eros eget nisl cursus sollicitudin. Nullam id mauris luctus, luctus diam at, consectetur nisl. Nullam iaculis arcu id mi pretium imperdiet. Nam sit amet risus ac velit fermentum commodo. Nam finibus mollis diam, sed auctor ipsum elementum quis.',
        'image': 'kind.svg',
        'reporter': 'kag@frett.is'
    },
    {
        'heading': 'Frétt 2',
        'content': 'Donec metus eros, congue eu urna sit amet, dapibus luctus elit. Ut a risus vel leo hendrerit commodo. Fusce mattis tristique rutrum. Proin in eros eget nisl cursus sollicitudin. Nullam id mauris luctus, luctus diam at, consectetur nisl. Nullam iaculis arcu id mi pretium imperdiet. Nam sit amet risus ac velit fermentum commodo. Nam finibus mollis diam, sed auctor ipsum elementum quis.',
        'image': 'kolkrabbi.svg',
        'reporter': 'kag@frett.is'
    },
    {
        'heading': 'Frétt 3',
        'content': 'Donec metus eros, congue eu urna sit amet, dapibus luctus elit. Ut a risus vel leo hendrerit commodo. Fusce mattis tristique rutrum. Proin in eros eget nisl cursus sollicitudin. Nullam id mauris luctus, luctus diam at, consectetur nisl. Nullam iaculis arcu id mi pretium imperdiet. Nam sit amet risus ac velit fermentum commodo. Nam finibus mollis diam, sed auctor ipsum elementum quis.',
        'image': 'snigill.svg',
        'reporter': 'dsg@frett.is'
    },
    {
        'heading': 'Frétt 4',
        'content': 'Donec metus eros, congue eu urna sit amet, dapibus luctus elit. Ut a risus vel leo hendrerit commodo. Fusce mattis tristique rutrum. Proin in eros eget nisl cursus sollicitudin. Nullam id mauris luctus, luctus diam at, consectetur nisl. Nullam iaculis arcu id mi pretium imperdiet. Nam sit amet risus ac velit fermentum commodo. Nam finibus mollis diam, sed auctor ipsum elementum quis.',
        'image': 'slanga.svg',
        'reporter': 'dsg@frett.is'
    }
]

@route('/')
def index():
    return template('tpl/verk3')


#########
#A HLUTI:
#########
@route('/a')
def lidura():
    return template('tpl/Ahluti')

@route('/kt/<kennitala>')
def kt(kennitala):
    return template('tpl/kennitala', kennitala=kennitala)


#########
# B HLUTI:
#########
@route('/b')
def lidurb():
    return template('tpl/index', frettir=frettir)

@route('/frett/<n>')
def frett(n):
    return template('tpl/frett', n=n, frettir=frettir)

#custom 404 error
@error(404)
def error404(error):
    return '<h2>Síða ekki til.</h2>'

####################
#static file routing
####################
#css files
@route('/static/css/<filename>')
def css(filename):
    return static_file(filename, root='static/css')

#img files
@route('/static/img/<filename>')
def img(filename):
    return static_file(filename, root='static/img')


run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
