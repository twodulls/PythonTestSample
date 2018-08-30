import pickle

'''
f = open("d:\workspace_python\Test\pickle_test.txt", 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()
'''
f = open("d:\workspace_python\Test\pickle_test.txt", 'rb')
data = pickle.load(f)
print(data)

