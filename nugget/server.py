from lxml import html
import requests

page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=TUFTS' +
					'+DINING&locationNum=11&locationName=Dewick-MacPhie' + 
					'+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus' +
					'&myaction=read&dtdate=3%2F31%2F2017')

page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=TUFTS' +
					'+DINING&locationNum=11&locationName=Dewick-MacPhie' + 
					'+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus' +
					'&myaction=read&dtdate=4%2F1%2F2017')

page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=TUFTS' +
					'+DINING&locationNum=11&locationName=Dewick-MacPhie' + 
					'+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus' +
					'&myaction=read&dtdate=4%2F2%2F2017')

page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=TUFTS' +
					'+DINING&locationNum=11&locationName=Dewick-MacPhie' + 
					'+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus' +
					'&myaction=read&dtdate=4%2F3%2F2017')

page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=TUFTS' +
					'+DINING&locationNum=11&locationName=Dewick-MacPhie' + 
					'+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus' +
					'&myaction=read&dtdate=4%2F4%2F2017')

tree = html.fromstring(page.content)

foods = tree.xpath('//a[@name="Recipe_Desc"]/text()')

print 'Foods: ', foods