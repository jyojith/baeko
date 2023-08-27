# Bakery Sales and Recommender System

This repository contains scripts for generating synthetic bakery sales data, implementing a user-based recommender engine, and using linear regression to predict product demand. The generated data is used to demonstrate the recommender system and predictive analysis.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
  - [Python](#python)
  - [Ruby](#ruby)
- [Generating Data](#generating-data)
  - [Ruby Script](#ruby-script)
- [User-Based Recommender Engine](#user-based-recommender-engine)
  - [Python Script](#python-script)
- [Linear Regression for Demand Prediction](#linear-regression-for-demand-prediction)
  - [Python Script](#python-script-1)
- [Using LSTM(Long Short-Term Memory) ](#using-LSTM)
  - [Jupyter Notebook](#jupyter-notebook)
- [Conclusion](#conclusion)

## Introduction

This project showcases the following functionalities:
- Generation of synthetic bakery sales data with various bakery items, cities, and users.
- Implementation of a user-based recommender engine to recommend bakery items to users.
- Use of linear regression to predict the demand for bakery items based on their price and discount.

## Prerequisites

### Python

- Python 3.x
- Required libraries: pandas, scikit-learn, matplotlib

### Ruby

- Ruby
- Faker gem (`gem install faker`)


## Generating Data

### Ruby Script

To generate synthetic bakery sales data using Ruby, run the following script:

```bash
ruby generate_sample_data.rb
```

This will generate the following csv files in the directory:
- bakery_pos_data.csv
- bakery_city_info.csv
- user_info.csv

We use this data for our recommender and prediction engine

## User-Based Recommender Engine

The user-based recommender engine uses a cosine similarity approach to recommend bakery products to users based on their historical interactions.

### Python Script

To run the user-based recommender engine using Python, execute the following script:

```bash
python recommender.py
```

## Demand Forcasting

we a re using two different approaches for prediction of demand of the bakery products using different machine learning models

### Using Regression

The linear regression model is used to predict the demand for bakery products based on historical transaction data.

#### Python Script

To run the linear regression model for demand prediction using Python, execute the following script:

```bash
python regression.py
```

### Using LSTM(Long Short-Term Memory)

The LSTM model is also used to predict the demand for bakery products using really large datasets and multiple training epochs.

#### Jupyter Notebook

You can open the jupyter notebook using google-collabs by uploading the following notebook file:

```bash
training_demand_forecasting.ipynb
```

## Conclusion

Congratulations! You've successfully generated synthetic data for a bakery Point of Sale (POS) system, implemented a user-based recommender engine, and explored demand prediction using linear regression. This repository serves as a comprehensive example to showcase various aspects of data generation, recommendation systems, and predictive analytics.

Feel free to customize, extend, or adapt the code and concepts in this repository to suit your specific needs. Whether you're learning about data generation, recommendation engines, or predictive modeling, this project provides a solid foundation to build upon.

If you have any questions, feedback, or improvements to suggest, please don't hesitate to [open an issue](https://github.com/jyojith/baeko/issues) or [create a pull request](https://github.com/jyojith/baeko/pulls). Your contributions are valuable and can help enhance the project further.

Thank you for exploring this project! Happy coding!

## License

This project is licensed under the MIT License.
