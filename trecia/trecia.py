# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}


#
def get_dict_values(dict):
   naujas = []
   for key in dict:
     naujas.append(dict[key])
   return naujas
get_dict_values(audi)


