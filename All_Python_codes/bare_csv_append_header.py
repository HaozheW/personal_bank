filenames = ['loan_headers.csv', '2012HMDALAR - National.csv']
with open('C:/Skydrive/2014 Ontodia/National/National/Home_Loan/home_loan_doc.csv', 'w+') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			for line in infile:
				outfile.write(line)