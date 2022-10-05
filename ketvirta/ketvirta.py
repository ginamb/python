# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

class Movie:
    # title = None

    def __init__(self,title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget


    def was_expensive(self):
        return self.budget > (100 * 1000)
        #return True if self.budget > (100 * 1000) else False


if __name__ == '__main__':
   movie = Movie('Titanic', 'XX', 5000000)
   was_expensive = movie.was_expensive()
   print(f'Ar buvo brangu: {was_expensive}')
