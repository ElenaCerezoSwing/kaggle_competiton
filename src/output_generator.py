from modelize import get_linear_regression_model, get_k_neighbors_model, get_ridge_model, get_sgd_model, get_random_forest_model
from data_tasks import load_submission_data, save_data, get_dataframe_copy

def linear_model_generator(X, y, test):
    y_pred = get_linear_regression_model(X, y, test)
    sub = load_submission_data()
    sub_linear= get_dataframe_copy(sub)
    sub_linear['price'] = y_pred
    save_data(sub_linear, 'linear')

def k_neigh_model_generator(X, y, test):
    y_pred = get_k_neighbors_model(X, y, test)
    sub = load_submission_data()
    sub_k_neigh = get_dataframe_copy(sub)
    sub_k_neigh['price'] = y_pred
    save_data(sub_k_neigh, 'k_neigh')

def sgd_model_generator(X, y, test):
    y_pred = get_sgd_model(X, y, test)
    sub = load_submission_data()
    sub_sgd = get_dataframe_copy(sub)
    sub_sgd['price'] = y_pred
    save_data(sub_sgd, 'sgd')

def ridge_model_generator(X, y, test):
    y_pred = get_ridge_model(X, y, test)
    sub = load_submission_data()
    sub_ridge = get_dataframe_copy(sub)
    sub_ridge['price'] = y_pred
    save_data(sub_ridge, 'ridge')


def random_forest_model_generator(X, y, test):
  y_pred = get_random_forest_model(X, y, test)
  sub = load_submission_data()
  sub_random_forest = get_dataframe_copy(sub)
  sub_random_forest['price'] = y_pred
  save_data(sub_random_forest, 'random_forest')


