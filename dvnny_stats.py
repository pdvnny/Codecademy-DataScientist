# HELPFUL STATISTICS & DATA SCIECNE FUNCTIONS



#This code implements the PCA exactly as in MATLAB so as to be consistent.
#It takes in an n x d data matrix X and returns a d x d orthonormal matrix pcaX. 
#Each column of pcaX contains a basis vector, sorted by decreasing variance.

def pca(X):
    covX = np.cov(X,rowvar=False)
    [Lambda,Vtranspose] = np.linalg.eig(covX)
    neworder = np.argsort(-abs(Lambda))
    pcaX = Vtranspose[:,neworder]
    pcaX = pcaX.real

    return pcaX



def reduce_data(Xtrain,Xtest,k):
    mu_train = np.mean(Xtrain, axis=0)
    print("The dimensions of mu_train are {}".format(mu_train.shape))
    
    # Centering Xtest
    Xtest_cent = Xtest - mu_train       # should be (rows x 4096) - (1 x 4096) --- subtracting mu_train from each row
    Xtrain_cent = Xtrain - mu_train
    print("The dimensions of centered vectors are {}".format(Xtest_cent.shape))
    
    # Need PCA matrices/data -- NOTE: the eigen vectors come as the rows from the PCA function (I THINK)
    pcaX = pca(Xtrain)
    print("The dimensions of pcaX are {}".format(pcaX.shape))
    
    # extract the first k "ROWS" (specific to my approach) of pcaX
    Vk = pcaX[0:k,:].T   # extract certain rows and transpose
    print("The dimensions of the Vk are {}".format(Vk.shape))
    
    # multiplication to produce the reduced matrices
    Xtrain_reduced = Xtrain_cent @ Vk
    Xtest_reduced = Xtest_cent @ Vk
    
    #Your code should go above this line.
    if (Xtrain_reduced.shape[0]!=Xtrain.shape[0]):
        raise Exception("The number of rows in Xtrain_reduced is not the same as the number of rows in Xtrain.")
    elif (Xtest_reduced.shape[0]!=Xtest.shape[0]):
        raise Exception("The number of rows in Xtest_reduced is not the same as the number of rows in Xtest.")
    elif (Xtrain_reduced.shape[1]!=k):
        raise Exception("The number of columns in Xtrain_reduced is not equal to k.")
    elif (Xtest_reduced.shape[1]!=k):
        raise Exception("The number of columns in Xtest_reduced is not equal to k.")
        
    return Xtrain_reduced, Xtest_reduced