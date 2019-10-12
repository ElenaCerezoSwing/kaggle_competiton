from data_tasks import load_train_data, load_test_data, save_data, get_dataframe_copy
from cleaning import get_cleaner_data, get_random_forest_cleaner_data
from assign import assign_X_y, get_splitted_train_test, assign_y_to_submitted
from modelize import get_linear_regression_model, get_k_neighbors_model, get_ridge_model, get_sgd_model
from output_generator import linear_model_generator, k_neigh_model_generator, sgd_model_generator, ridge_model_generator, random_forest_model_generator
from standarize import get_standard_scaler


def main():
  print('starting etl')
  train = load_train_data()
  train_normal = get_dataframe_copy(train)
  test = load_test_data()
  test_normal = get_dataframe_copy(test)
  train_normal = get_cleaner_data(train_normal)
  train_normal = train_normal.dropna()
  test_mormal = get_cleaner_data(test_normal)
  X_normal, y_normal = assign_X_y(train_normal)
  linear_model_generator(X_normal, y_normal , test_mormal)
  k_neigh_model_generator(X_normal, y_normal , test_mormal)
  sgd_model_generator(X_normal, y_normal , test_mormal)
  ridge_model_generator(X_normal, y_normal , test_mormal)
  print('processing randomForest Model')
  X, y = assign_X_y(train)
  X_test = test
  X_test = get_random_forest_cleaner_data(X_test)
  X = get_random_forest_cleaner_data(X)
  X_transform, X_test_transform = get_standard_scaler(X, X_test)
  X_transform = X_transform.fillna(0)
  X_test_transform = X_test_transform.fillna(0)
  random_forest_model_generator(X_transform, y, X_test_transform)

if __name__ == '__main__': 
  main()