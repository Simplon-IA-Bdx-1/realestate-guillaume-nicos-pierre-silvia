class Annonce(dict):

    fields = ['idannonce', 'typedebien', 'codepostal',
              'codeinsee', 'ville', 'idtypechauffage',
              'idtypecuisine', 'si_balcon', 'nb_chambres', 
              'nb_pieces', 'si_sdbain', 'si_sdEau', 'nb_photos', 'etage',
              'prix', 'surface', 'dpeL', 'dpeC', 'description', 'id']

    mandatory_fields = ['idannonce', 'prix']
   
    def __init__(self, **kwargs):

        for key in self.mandatory_fields:
            if key not in kwargs:
                raise Exception('{} field is mandatory'.format(key) )

        for key,value in kwargs.items():
            if key in self.fields:
                self[key] = value
            else:
                raise Exception('{} is not a valid field'.format(key))
                
# Return a list containg all values in the same order as Annonce.fields
# in order to be passed as data with a prepared statement
# or to write a csv file with csv.writer
    def get_all_values(self):
        """Gets all values for all fields of the ad."""
        values = []
        for key in self.fields:
            values.append(self.get(key, None))
        return values

# Return a string with all fields in order in the format "('field1', 'field2, ...)"
# in order to be used to build a SQL query
    def get_all_fields_as_string(self):
        """Returns a string vector containing all fields."""
        strings = []
        for key in self.fields:
            strings.append("`{}`".format(key))
        return "(" + ", ".join(strings) + ")"

    def get_fields(self):
        """Get fields but separately."""
        return list(self.keys())

# Return the list of defined fields (not None) in the same order as get_fields()
    def get_values(self):
        """Get values but separately."""
        return list(self.values())

    def get_fields_as_string(self):
        """Returns a string vector containing all values of all fields."""
        strings = []
        for key in self.keys():
            strings.append("`{}`".format(key))
        return "(" + ", ".join(strings) + ")"

import csv

# Write a csv file from a list of Annonce objects
def to_csv(filename, annonces):
    """Write a csv file from a list of Annonce objects"""
    with open(filename, "w", encoding='utf-8', newline='\n') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(annonces[0].fields)
        for annonce in annonces:
            annonce_list = annonce.get_all_values()
            desc_index = Annonce.fields.index('description')
            #print(annonce_list[desc_index].replace("\n","\\n").replace("\r","\\r"))
            annonce_list[desc_index] = annonce_list[desc_index].replace("\n", "\\n").replace("\r", "")
            writer.writerow(annonce_list)

    
if __name__ == "__main__":
    #annonce = Annonce(idannonce=12345, prix=123456, description='texte, texte.')
    annonce = Annonce(idannonce=12345, prix=123456)
    
    print("\tannonce.get_all_fields_as_string() ->")
    print("\"" + annonce.get_all_fields_as_string() + "\"")
    print("\ttuple(annonce.get_all_values()) ->")
    print(tuple(annonce.get_all_values()))
    print("\tannonce.get_fields() ->")
    print(annonce.get_fields())
    print("\tannonce.get_fields_as_string() ->")
    print("\"" + annonce.get_fields_as_string() + "\"")
    print("\ttuple(annonce.get_values()) ->")
    print(tuple(annonce.get_values()))

    to_csv('test.csv', [annonce])



"""
idannonce (int(11) - CLE PRIMAIRE - AUTOINCREMENT) : Code du bien concerné par la recherche. Exemple: 155142519
typedebien (int(11)) : Définit le type logement. Exemple: Appartement
position (int(11)) : ??? Exemple: 0 ou 1
codepostal (int(11)) : Code postal de la ville où est situé le bien. Exemple: 75002
codeinsee (int(11)) : Numéro composé du code postal ainsi que le numéro du quartier. Exemple: 75102
ville (varchar(255)) : Situation géographique du bien concerné. Exemple: Paris
idtypechauffage (varchar(255)) : Caractéristiques du chauffage du bien (si chauffage). Exemple: individuel électrique
idtypecuisine (varchar(255)) : 0 si pas de cuisine / 1 si cuisine. Exemple: 0 ou 1
naturebien (tinyint(4)) : ???. Exemple: 0 ou 1
si_balcon (tinyint(4)) : 0 si pas de balcon / 1 si balcon. Exemple: 0 ou 1
nb_chambres (tinyint(4)) : Nombre de chambres dans le logement. Exemple: 2
nb_pieces (tinyint(4)) : Nombre de pièces dans le logement. Exemple: 2
si_sdbain (tinyint(4)) : 0 si pas de baignoire / 1 si baignoire. Exemple: 0 ou 1
si_sdEau (tinyint(4)) : 0 si pas de douche / 1 si douche. Exemple: 0 ou 1
nb_photos (tinyint(4)) : Nombre de photos présentes dans l'annonce. Exemple: 3
prix (smallint(6)) : Montant du loyer mensuel, charges comprises. Exemple: 750
surface (smallint(6)) : Surface habitable en m2. Exemple: 95
dpeL (varchar(10)) : ???. Exemple: 0 ou 1
dpeC (varchar(10)) : ???. Exemple: 0 ou 1
"""
