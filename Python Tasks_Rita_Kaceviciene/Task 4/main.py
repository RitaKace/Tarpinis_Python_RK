# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def wasExpensive(self):
        if self.budget > 100000000:
           expensive = True
        else:
           expensive = False
        
        return expensive

mowie1 = Movie("The Handmaid`s Tale", "Bruce Miller", 200000000)
mowie2 = Movie("Bad mowie", "P M", 5000000)



print("Movie1 was expensive: ",mowie1.wasExpensive())

print("Mowie2 was expensive: ",mowie2.wasExpensive())