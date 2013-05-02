"""
Scrapes MAL for animedata given a URL starting link!
No parallelization because currently Google App Engine doesn't have much in the way of free computing power :/ and I don't want to accidentally eat a ton of MAL's server resources
"""
DEPTH = 20
NODE_SIZE_SCALE=100
Filename='MALgraph.gexf'
def make_graph():
	import re,urllib,networkx as nx
	##pylab as plt
	from collections import deque
	from math import sqrt,exp
	
	"""
	Wanted to use Matplotlib's colormaps but it seems installing it via pip is a pain, so instead I'm using an interpolating function for one of them: "RdBu"
	"""
	print "[-] Graph Making Started"
	print "[-] Started Web Scraping"
	url="http://myanimelist.net/anime/3389/Bus_Gamer/userrecs"
	pattern = re.compile('(?<=<div style="margin-bottom: 2px;"><a href=").*?(?=")')
	G = nx.Graph()
	q = deque([[(x[29:]).split('/') for x in [url]][0][0:2]])
	for x in range(DEPTH):
	    print '--> Working on ' + str(x)
	    ci,cn = q.popleft()
	    urld = urllib.urlopen("http://myanimelist.net/anime/"+ci+"/"+cn+"/userrecs").read()
	    d = [(x[29:]).split('/') for x in pattern.findall(urld)]
	    for z in d:
		q.append((z[0],z[1]))
		G.add_edge(unicode(cn,'utf-8'),unicode(z[1],'utf-8'))
	print '[X] Finished Web Scraping'
	###Locally I'll just use Matplotlib. In Heroku I doubt it will work
	def colormap(g):
		print '[-] Started Coloring'
		#what matplotlib color map?
		CMAP1="Paired"
		CMAP2="Paired"
		from matplotlib.cm import get_cmap
		cmap1 = get_cmap(name=CMAP1)
		cmap2 = get_cmap(name=CMAP2)
		maxdegree=max(g.degree(g.nodes()).values())
		for y in g.nodes():
			ratio = 1.0*g.degree(y)/maxdegree
			c = cmap1(2*ratio) if ratio<=.5 else cmap2(2*ratio)
			g.node[y]['viz']={'color':{'r':255*c[0],'g':255*c[1],'b':255*c[2],'a':0},'size': exp(ratio)*NODE_SIZE_SCALE}
		print '[X] Finished Coloring'		

	colormap(G)

#nx.draw(G)
	#plt.show()
	nx.write_gexf(G,"static/"+Filename,version="1.2draft")
	print '[X] Saved to file'
if __name__=='__main__':
	make_graph()
	print '[X] Graph Made'
