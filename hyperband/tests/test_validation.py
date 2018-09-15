from nose.tools import raises
from hyperband import HyperbandSearchCV

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint as sp_randint


def setup():
    model = RandomForestClassifier()
    param_dist = {"max_depth": [3, None],
                  "max_features": sp_randint(1, 11),
                  "min_samples_split": sp_randint(2, 11),
                  "min_samples_leaf": sp_randint(1, 11),
                  "bootstrap": [True, False],
                  "criterion": ["gini", "entropy"]}

    return model, param_dist


@raises(ValueError)
def test_check_min_iter():
    model, param_dist = setup()
    HyperbandSearchCV(model, param_dist, min_iter=-1)._validate_input()
    HyperbandSearchCV(model, param_dist, min_iter='test')._validate_input()


@raises(ValueError)
def test_check_max_iter():
    model, param_dist = setup()
    HyperbandSearchCV(model, param_dist, max_iter=-1)._validate_input()
    HyperbandSearchCV(model, param_dist, max_iter='test')._validate_input()


@raises(ValueError)
def test_check_min_iter_smaller_max_iter():
    model, param_dist = setup()
    HyperbandSearchCV(model, param_dist, min_iter=30, max_iter=15)._validate_input()


@raises(ValueError)
def test_check_skip_last():
    model, param_dist = setup()
    HyperbandSearchCV(model, param_dist, skip_last=-1)._validate_input()
    HyperbandSearchCV(model, param_dist, skip_last='test')._validate_input()


@raises(ValueError)
def test_check_eta():
    model, param_dist = setup()
    HyperbandSearchCV(model, param_dist, eta=0)._validate_input()
    HyperbandSearchCV(model, param_dist, eta='test')._validate_input()


@raises(ValueError)
def test_check_eta():
    model, param_dist = setup()
    HyperbandSearchCV(model, param_dist, resource_param='wrong_name')._validate_input()


@raises(ValueError)
def test_warm_start_keys():
    model, param_dist = setup()
    model = KNeighborsClassifier()
    HyperbandSearchCV(model, param_dist, resource_param='n_neighbors', warm_start=True)._validate_input()


@raises(ValueError)
def test_warm_start_type():
    model, param_dist = setup()
    HyperbandSearchCV(model, param_dist, warm_start='test')._validate_input()
