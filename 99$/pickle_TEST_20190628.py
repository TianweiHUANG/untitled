import time
import pickle

a_dict={'wpp':'htw','hyy':'cjx','zlj':'htb','mama':'baba'}

file=open('pickle_TEST.pickle','wb')
pickle.dump(a_dict,file)
file.close()

time.sleep(10)

file=open('pickle_TEST.pickle','rb')
a_dict1=pickle.load(file)
file.close()

print(a_dict1)
