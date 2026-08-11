import pandas as pd
import numpy as np
import sys

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

TEST_SIZE = 0.2


# loading data
def load_data(filename):

    df = pd.read_csv(filename)

    print("Dataset shape : ")
    print(df.shape)

    print("\nFirst row : ")
    print(df.info())

    print("\nDataset information : ")
    print(df.info())

    return df


def prepare_data(df):
    """
    Separate the dataset into :
    X = features used to predict the price
    y = SalePrice, the target we want to predict
    """

    y = df["SalePrice"]

    X = df.drop(columns="SalePrice")

    print("\nX shape:", X.shape)
    print("y shape:", y.shape)

    return X, y


def identify_features(X):
    """
    Identify numerical and categorical features

    Numerical Features are columns containing integers or floating-point numbers

    Categorical features are columns containing text/categories.

    Returns:
        numerical_features, categorical_features
    """

    numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

    print("\nNumerical Features:")
    print(numerical_features)

    print("\nCategorical Features:")
    print(categorical_features)

    return numerical_features, categorical_features


def create_preprocessor(numerical_features, categorical_features):
    """
    Create the preprocessing pipeline
    Numerical features:
      -Missing values are replaced by the median.
    Categorical Features:
       - Missing values are replaced by the most frequent value.
       - Categories are converted using One-Hot Encoding

    Returns:
        A ColumnTransformer
    """

    numerical_pipeline = Pipeline([("imputer", SimpleImputer(strategy="median"))])

    categorical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        [
            ("numerical", numerical_pipeline, numerical_features),
            ("categorical", categorical_pipeline, categorical_features),
        ]
    )

    return preprocessor


def train_model(preprocessor, X_train, y_train):
    """
    Create and train a linear regression model.
    The preprocessing is included in the pipeline so that the same transformations are applied during training and
    prediction.
    Returns:
       A fitted model.
    """

    model = Pipeline(
        [("preprocessor", preprocessor), ("regressor", LinearRegression())]
    )

    model.fit(X_train, y_train)

    return model


def evaluate(y_true, predictions):
    """
    Evaluate the model using:
    MAE
    MSE
    RMSE
    R^2
    """

    mae = mean_absolute_error(y_true, predictions)

    mse = mean_squared_error(y_true, predictions)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_true, predictions)

    print("\n==============================")
    print("MODEL EVALUATION")
    print("==============================")
    print(f"MAE : {mae:.2f}")
    print(f"MSE : {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R² : {r2:.4f}")

    print("\nFirst predictions:")
    results = pd.DataFrame({"Actual": y_true.values, "Predicted": predictions})
    print(results.head(10))


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python house_price.py data")

    # Load data
    df = load_data(sys.argv[1])

    # Separate features and target
    X, y = prepare_data(df)

    # Identify numerical and categorical features
    numerical_features, categorical_features = identify_features(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=42
    )

    print("Training set: ", X_train.shape)
    print("Test set: ", X_test.shape)

    # Create preprocessing pipeline
    preprocessor = create_preprocessor(numerical_features, categorical_features)

    # Train model
    model = train_model(preprocessor, X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate model
    evaluate(y_test, predictions)


if __name__ == "__main__":
    main()
