# from collections import Counter

# lst = ['john\ndickinson', "m'uzuri", 'joachim', 'thomas', 'emerson', 'james\nstephen', 'flaubert', 'aga\nkhan', 'adam\napple', 'jackson\nphillip', "m'usuri", 'josie', 'andré\nmasson', 'richard\ncarvell', 'kalal', 'harry\nstanley', 'david\ngarrick', 'barrett\nmccullough', 'charles\nlaughton', 'fred\nastaire', 'paulino', 'charlie\ncurtis', 'ben\ngallagher', 'clara', 'robert', 'captain', 'eric\ndorman-smith', 'florence', 'uffizi\npitti', "d'annunzio", 'isonzo\nbainsizza', 'robert', 'gabriele', 'michele', 'baron\nvii', 'carpano', 'brusadelli', 'giorgio', 'ronald', 'jesus', 'kenya', 'ettore', 'barone\nandrea', 'renata', 'carlo\nricardo', 'richard', 'diana', 'dante\nvieux\nfirenze', 'georgie\npatton', 'crudo', 'erwin\nrommel', 'bernard', 'maurice\nsaxe', "frederick\nt'sun", 'marie\nantoinette', 'velasquez', 'wassermann', 'ida\nlupino', 'pete\nquesada', 'othello', '-eifel', 'toi\nrimbaud', 'valentine', 'thomas\nj', 'john\nnicanor', 'robert\ncohn', 'princeton', 'robert', 'jake', 'hudson', 'jacob', 'clyne', 'leblanc', 'monsieur', 'etienne\ndu', 'crillon', 'michel', 'aloysius\nkirby', 'monte\ncarlo', 'paix', 'paula\nritz', 'hardy\nanatole', 'michael\nsan\nsebastian', 'baron', 'jefferson', 'davis', 'dred\nscott', 'frankie\nfritsch', 'fordham', 'wayne\nb\nwheeler', 'davidson', 'harris', 'jolly', 'fourth\nwilson', 'harris', 'juanito', 'pedro\nromero', 'carlos', 'marcial\nlalanda\nmarquez', 'mike', 'christ', 'charley\nblackman', 'jeronimo', 'evan', 'manuel\ngarcia', 'miguel\nretana', 'antonio\nnovillero', 'charlie\nchaplins', 'cogida', 'manos\nmanosduros', 'joselito\nbelmonte', 'el\nheraldo', 'campagnero\nnegro', 'arditi', 'signor', 'george', 'nick\nadams', 'ole\nandreson', 'willard', 'toledo\nlardner', 'john\ncollins', 'irishman', 'christ', 'frank', 'mitchell\nhollow', 'william\ncampbell', 'jesus', 'aim\nbritton', 'dr\nvan\ndyke', 'nancy\nhawthorne', 'manuel\ngarcia', 'antonio\nnovillero', 'charlie\nchaplins', 'manos\nmanosduros', 'joselito', 'veronica', 'arditi\nsort', 'george', 'nick\nadams', 'ole\nandreson', 'toledo\nlardner', 'john\ncollins', 'christ\nwake\nlew', 'kelly', 'billy\ntabeshaw', 'frank', 'mitchell\nhollow', 'palermo']
# loc_lst = [i if "\n" not in i else ' '.join(j for j in i.split('\n')) for i in lst]

# a = Counter(loc_lst)

# print(a)

#for i in loc_lst:
 #   print(i)
 

import wikipedia
import re
from pathlib  import Path


temp_txt = Path('locations.txt').read_text()
new_list = []

for i in temp_txt.split():
 try:
  txt_sum = wikipedia.summary(i)
  if 'city' in txt_sum.split()[:25]:
   print('city: {}'.format(i))
  elif 'country' in txt_sum.split()[:25]:
   print('country: {}'.format(i))
  elif 'state' in txt_sum.split()[:25]:
   print('state: {}'.format(i))
  else:
   new_list.append((i,'UNK'))
 except:
  new_list.append((i,'No Data'))
print(new_list)
