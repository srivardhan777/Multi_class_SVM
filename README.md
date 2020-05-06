# Multi_class_SVM

CODE IMPLEMENTATION


COEFFICIENTS:

The coefficients should be chosen in such a way that the first set of alpha values are taken as it is. In second set of alpha values its first row all the terms are made negative except the first element. Similarly, in second set of alpha values first two rows are made negative except the first 2 terms in second row. Similarly, in nth row all the first (n-1) rows should be made negative except the (n-1) elements in the (n-1)th row. This pattern should be followed when initializing the alpha values.


SUPPORT VECTORS:

Support vectors are taken as it is from the data of support vectors. Support vectors are in the form of matrices. It should have the columns equal to the vector dimension and rows equal to the number of support vectors.


MULTICLASS:

The inbuilt code works only for single class. I have made certain changes to make it a multiclass support vector machine (SVM). I have removed the initialized array size and kept it empty. I have taken two nested for loops and called the svm_predict( ) for each vector dimension number of elements inside these nested loops. Then we can get the respective class for each row inside the input array i.e., sensors.
