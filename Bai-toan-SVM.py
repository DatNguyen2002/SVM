from sklearn.svm import SVC

model = SVC(kernel='linear', probability=True)
model.fit(emb_array, labels)
#Do somethings....
w = model.coef_
b = model.intercept
print('w = ', w)
print('b = ', b)