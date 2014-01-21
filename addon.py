from xbmcswift2 import Plugin
import radionational 

plugin = Plugin()


@plugin.route('/')
def index():
	output = radionational.get_podcasts()
	items = []
	for i in output:
		item = {'label':i['title'],'path':i['url'], 'is_playable': True}
		items.append(item)
   
	return items

if __name__ == '__main__':
    plugin.run()

