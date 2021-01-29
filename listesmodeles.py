from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor


def modelist():
    modeles = []
    modeles.append(LinearRegression())

    for val_alpha in (1e-3, 1e-2, 1e-1, 1):
        modeles.append(Lasso(alpha=val_alpha))

    for val_alpha in (1e-3, 1e-2, 1e-1, 1):
        modeles.append(Ridge(alpha=val_alpha))

    for val_alpha in (1e-3, 1e-2, 1e-1, 1):
        for val_l1 in (0.25, 0.5, 0.75):
            modeles.append(ElasticNet(alpha=val_alpha, l1_ratio=val_l1))

    for nb_voisins in range(3, 10):
        modeles.append(KNeighborsRegressor(n_neighbors=nb_voisins))



    for val_epsilon in (10 ** n for n in range(-3, 1)):
        for val_C in (10 ** n for n in range(-3, 4)):
            modeles.append(SVR(epsilon=val_epsilon, C=val_C))


    for nb_estimateurs in (50, 100, 150, 200):
        modeles.append(RandomForestRegressor(n_estimators=nb_estimateurs))

    for nb_neurones in  ((100,), (50, 50), (25, 50, 25)):
        modeles.append(MLPRegressor(hidden_layer_sizes=nb_neurones))
        
    return modeles