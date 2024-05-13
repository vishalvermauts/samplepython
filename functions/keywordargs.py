def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_bikes(**bikes):
	print("My best bike is " + bikes['best'])
 
 
my_bikes(best='honda',bestest='CBR')
