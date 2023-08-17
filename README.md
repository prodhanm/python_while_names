The purpose of this coding exercise is to be able to use a while loop to create a dictionary. The purpose of the while loop is that, if there are no set of object data, such as a complete list, dictionary, sets, or a tuple, then a while loop can be used to add data into a data set. 

In this exercise, we want to create a family dictionary. Each key represents, a family relationship in a supposed family tree like structure of the dictionary. Such aspects of the family relationship can be demonstrated below:

                    family relationship:
                        1. father
                        2. mother
                        3. son/daughter
                        4. sibling to the father/mother
                        5. grandparents
                        6. relatives
                        7. other

The family relationship can then be tied to the name of one of the options. Each time, a relatinship is added, a name has to be added. Once that is done and one has completed their family dictionary listings, the following dictionary is created:

            family = {
                'father': 'name', 
                'mother': 'name', 
                'son': 'name', 
                'sister': 'name', 
                'Grandfather': 'name', 
                'Grandmother': 'name'
            }

Once this dictionary is created, the main() then calls the name_li(fmaily) to proceed with a dictionary for loop. The loop organizes, the family relationship to their names as such:

                father: name 
                mother: name 
                son: name 
                sister: name 
                Grandfather: name 
                Grandmother: name
