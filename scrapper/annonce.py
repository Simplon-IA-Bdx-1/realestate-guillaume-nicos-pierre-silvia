class Annonce(dict):

    fields = ['idannonce', 'codepostal', 'prix', 'surface',
                 'typedebien', 'position', 'codepostal', 'codeinsee',
                 'ville', 'idtypechauffage', 'idtypecuisine', 
                 'naturebien', 'si_balcon', 'nb_chambres', 
                 'nb_pieces', 'si_sdbain', 'si_sdEau', 'nb_photos', 
                 'prix', 'surface', 'dpeL', 'dpeC']

    mandatory_fields = ['idannonce', 'prix']
   
    def __init__(self, **kwargs):

        for key in self.mandatory_fields:
            if key not in kwargs:
                raise Exception('{} field is madatory'.format(key) )

        for key,value in kwargs.items():
            if key in self.fields:
                self[key] = value

"""
idannonce (int(11) - CLE PRIMAIRE - AUTOINCREMENT) : Code du bien concerné par la recherche. Exemple: 155142519 ;
typedebien (int(11)) : Définit le type logement. Exemple: Appartement ;
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
