#---------------------------------------------------#
#---------------The ARGANS Dictionary---------------#
#---------------------------------------------------#

choice=None
dictionary={"DIMITRI": "Database for Imaging Multi-spectral Instruments and Tools for Radiometric Intercomparison",
            "AC":"Atmospheric Correction",
            "BRDF":"Bidirectional Radiance Distribution Function",
            "TOA":"Top Of Atmosphere",
            "Rho":"Reflectance"}

while choice!=0:
    print """
	ARGANS Translator

	0 - Quit
	1 - Look up a term
	2 - Add a term
	3 - Redefine a term
	4 - Delete a term
	"""

    choice=int(raw_input("What is your choice?: "))
    print
	
	# exit
    if choice==0:
        print"Good-bye."

	# get a definition
    elif choice==1:
        term=raw_input("What term do you want me to translate?: ")
        if term in dictionary:
            definition=dictionary[term]
            print
            print term,"means",definition	
        else:
            print"Sorry I don't know the term:", term

	# add a term-definition pair
    elif choice==2:
        term=raw_input("What term do you want me to add?: ")
        if term not in dictionary:
            definition=raw_input("\nWhat is the definition?: ")
            dictionary[term]=definition
            print"\n", term, "has been added."
        else:
            print"\nThat term already exists."

    # redefinie an existing term
    elif choice==3:
        term=raw_input("What term do you want me to redifine?: ")
        if term in dictionary:
            definition=raw_input("What is the new definition?: ")
            dictionary[term]=definition
            print"\n", term, "has been redifined."
        else:
            print"\nThat term already exists."

    elif choice==4:
        term=raw_input("What term do you want me to delete?: ")
        if term in dictionary:
            del dictionary[term]
            print"\nThe term", term, "is deleted."
        else:
            print"\nIt's impossible.", term, "doesnt't exist in the dictionary."
    
    # invalide choice
    else:
        print"\nSorry, but", choice, "isn't a valid choice."

raw_input("\n\nPress the ENTER key to exit.")        

 


