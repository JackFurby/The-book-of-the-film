import glob, os
import rdflib
from rdflib import Namespace
from tqdm import tqdm


# Add all RDF file to a list
root = "./rdf_info/epub/**"
bookfiles = []
for file in glob.glob(root + "/*.rdf", recursive=True):
	bookfiles.append(file)


# RDF namespaces
dctermsNs = Namespace("http://purl.org/dc/terms/")
pgtermsNs = Namespace("http://www.gutenberg.org/2009/pgterms/")


# For each RDF file in list extract title, id and link and add to dict and dict to list
bookList = []
for i in tqdm(range(len(bookfiles))):
	g = rdflib.Graph()
	g.load(bookfiles[i])

	book = {}
	for subj, pred, obj in g:
		if pred == dctermsNs.title:
			book["title"] = str(obj)
		if obj == pgtermsNs.ebook:
			#print(subj.split("/")[-1])
			book["id"] = subj.split("/")[-1]
		if obj == pgtermsNs.file:
			if subj[-4:] == '.txt':
				book["link"] = str(subj)
	#print(book)

	bookList.append(book)

for i in bookList:
	print(i)
