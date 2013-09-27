#!/usr/bin/python
import sys, getopt, csv

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError :
		print 'phanikumar-3.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts :
		if opt == '-h' :
			print 'phanikumar-3.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile") :
			inputfile = arg
		elif opt in ("-o", "--ofile") :
			outputfile = arg
	if inputfile == '' or  outputfile == '' :
		print 'phanikumar-3.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	processfile(inputfile,outputfile)

def processfile(inputfile,outputfile):
	companies = {}
	with open(inputfile, 'rb') as csvfile :
		reader = csv.reader(csvfile,  delimiter=',',  quotechar='|')
		header = reader.next()
		header = map(str.strip, header)
		for x in header[2:] :
			companies[x] = {'YearMonth' : [],'Value' : 0}
			
		for row in reader :
			i = 2
			row = map(str.strip, row)
			if row[i] is not None :
				for comapny in companies :
					if companies[comapny]['Value'] < int(row[i]) :
						companies[comapny]['Value'] = int(row[i])
						companies[comapny]['YearMonth'] = [row[0]+'-'+row[1]]
					elif companies[comapny]['Value'] == int(row[i]) :
						companies[comapny]['YearMonth'].append(row[0]+'-'+row[1])
					i = i + 1
		
	with open(outputfile, 'wb') as csvfile :
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Company Name', 'Highest Value', 'Year-Month'])
		for comapny in companies :
			data = [comapny, companies[comapny]['Value'], ' & '.join(companies[comapny]['YearMonth'])]
			writer.writerow(data)

if __name__ == "__main__" :
	main(sys.argv[1:])
