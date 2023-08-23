from invert_func import *

docs=[]
for i in range (1,5):
    file = open(r"C:\Users\PATH_TO_YOUR_TEXT_DOCS"+str(i)+".txt",'r')
    file=file.read()
    docs.append(file)

# Create an instance of InvIndex
inv_ind=InvIndex(docs)

# Perform a sample query and print the matching documents
print(inv_ind.run_query('A string from one of these docs'))

