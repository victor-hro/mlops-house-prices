# MLOps House Prices

Web App for House Price Prediction encapsulated in a Docker container.

This project provides an interactive web application to forecast house prices based on Machine Learning models. The entire codebase is encapsulated within a Docker container for easy execution and deployment.

## How to Run with Docker

To run this project using Docker, follow these steps:

### Prerequisites

- Docker installed on your machine.

### Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/seu-usuario/mlops-house-prices.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mlops-house-prices
   ```

3. Build the Docker image:

   ```bash
   docker build -t house-price-prediction .
   ```

4. Run the Docker container:

   ```bash
   docker run -p 8501:8501 house-price-prediction
   ```

5. Access the web application:

   Open your web browser and go to `http://localhost:8501` to access the House Price Prediction web app.

### Docker Compose

Alternatively, you can use Docker Compose:

1. Ensure Docker Compose is installed.

2. Run the following command:

   ```bash
   docker-compose up
   ```

This will start the application and make it available at `http://localhost:8501`.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io