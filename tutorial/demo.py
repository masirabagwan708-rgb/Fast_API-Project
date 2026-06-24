def add(firstname:str| list,lastname:str = None):
    firstname.capitalize()
    return firstname + " " + lastname
fname="Nill"
lname="Gates"

Name= add(fname ,lname)
print(Name)