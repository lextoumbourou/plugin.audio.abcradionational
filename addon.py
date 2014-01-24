from xbmcswift2 import Plugin
import radionational

plugin = Plugin()

#title menu
@plugin.route('/')
def index():
    items = [{'label': "Just In", 'path': plugin.url_for('just_in')},
             {'label': "Programs", 'path': plugin.url_for('programs')},
             {'label': "Subjects", 'path': plugin.url_for('subjects')}]
    return items

#the 'just in' menu: all playable from here
@plugin.route('/just_in/')
def just_in():
    items =[]
    output = radionational.get_podcasts("http://abc.net.au/radionational/podcasts")
    for i in output:
        item = {'label':i['title'],'path':i['url'], 'is_playable': True}
        items.append(item)
    return items

#the programs menu: non playable
@plugin.route('/programs/')
def programs():
    items = []
    output = radionational.define_program_url()
    for i in output:
        item = {'label':i['title'],'path':i['url']}
        items.append(item)
    return items

#i need to find the <program_id> and link it to the url and just use exsting get_podcast()
@plugin.route('/programs/<program_id>')
def open_programs(program_id):
    items = []


@plugin.route('/subjects/')
def subjects():
    items =[]
    output = radionational.define_program_url("http://abc.net.au/radionational/subjects")
    for i in output:
        item = {'label':i['title'],'path':i['url'], 'is_playable': True}
        items.append(item)
    return items


if __name__ == '__main__':
    plugin.run()

