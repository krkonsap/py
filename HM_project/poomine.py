import random

def poomine():
  kriips = "-" * len(lahendus)
  pakkumiste_arv = 10
  while pakkumiste_arv > 0 and not kriips == lahendus:
    print("Otsitav sõna: " + kriips)
    print ("Pakkumisi järel: " + str(pakkumiste_arv))
    pakkumine = input("Pakkumine:")
    
    if len(pakkumine) != 1:
      print ("Pakkumiseks saab olla ainult üks tähemärk!")
    elif pakkumine in lahendus:
      print ("See täht on lahenduses!")
      kriips = kriips_uuendus(lahendus, kriips, pakkumine)
    else:
      print ("Täht puudub lahendusest!")
      pakkumiste_arv -= 1
    
  if pakkumiste_arv < 1:
    print ("Kaotus.. Otsitav sõna oli: " + str(lahendus))
  else:
    print ("Õnnitlused! Sõnaks oli: " + str(lahendus))
    
def kriips_uuendus(lahend, kriips_u, arvatud):
  tulemus = ""
  
  for i in range(len(lahend)):
    if lahend[i] == arvatud:
      tulemus = tulemus + arvatud
    else:
      tulemus = tulemus + kriips_u[i]
      
  return tulemus
    
sonad_fail = open('sonad.txt')
sonad = sonad_fail.read().splitlines()

lahendus = random.choice(sonad)
poomine()