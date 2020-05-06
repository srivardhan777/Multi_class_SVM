import numpy as np
X = np.array([[3,4],[1,4],[2,3],[6,-1],[7,-1],[5,-3]] )
y = np.array([-1,-1, 1, -1, 1 , 1 ])
from sklearn.svm import SVC
clf = SVC(C = 0.01, kernel = 'linear')
clf.fit(X, y) 
sv1 = clf.support_vectors_
coeff=np.abs(clf.dual_coef_)
print('w = ',clf.coef_)
print('b = ',clf.intercept_)
print('Indices of support vectors = ', clf.support_)
print('Support vectors = ', clf.support_vectors_)
print('Number of support vectors for each class = ', clf.n_support_)
print('Coefficients of the support vector in the decision function = ', np.abs(clf.dual_coef_))