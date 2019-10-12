from data_tasks import load_train_data, load_test_data, save_data
from cleaning import get_cleaner_data
from assign import assign_X_y, get_splitted_train_test, assign_y_to_submitted
from modelize import get_linear_regression_model, get_k_neighbors_model, get_ridge_model, get_sgd_model
from output_generator import linear_model_generator, k_neigh_model_generator, sgd_model_generator, ridge_model_generator

def main():
  print('starting etl')
  train = load_train_data()
  test = load_test_data()
  train = get_cleaner_data(train)
  train = train.dropna()
  test = get_cleaner_data(test)
  X, y = assign_X_y(train)
  linear_model_generator(X, y, test)
  k_neigh_model_generator(X, y, test)
  sgd_model_generator(X, y, test)
  ridge_model_generator(X, y, test)


if __name__ == '__main__': 
  main()