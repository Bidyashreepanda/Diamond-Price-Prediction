# 💎 Diamond Price Prediction Using Machine Learning

<p align="center">
  <strong>Predict diamond prices using K-Nearest Neighbors (KNN) Regression and deploy an interactive web app with Streamlit.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-KNN-orange" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Project Status">
</p>

---

## 📌 Project Overview

How much is a diamond worth? 💎

Diamond prices depend on several factors, including carat weight, cut quality, color, clarity, and physical dimensions. In this project, I built a machine learning model that predicts diamond prices based on these characteristics.

The project uses **K-Nearest Neighbors (KNN) Regression** and provides a user-friendly web interface built with **Streamlit**, allowing users to enter diamond details and receive an estimated price.

## 🎯 Objectives

- Understand and explore diamond price data.
- Clean and preprocess the dataset.
- Encode categorical variables and scale numerical features.
- Train a KNN Regression model.
- Evaluate model performance using regression metrics.
- Save the trained model using Pickle.
- Deploy an interactive prediction application using Streamlit.

## 📂 Dataset

The project uses a diamond dataset containing information about diamond characteristics and their prices.

| Column | Description |
|---|---|
| `carat` | Weight of the diamond |
| `cut` | Quality of the cut |
| `color` | Diamond color grade |
| `clarity` | Diamond clarity grade |
| `depth` | Total depth percentage |
| `table` | Width of the top surface relative to the widest point |
| `x` | Length in millimeters |
| `y` | Width in millimeters |
| `z` | Depth in millimeters |
| `price` | Target variable: diamond price |

## ⚙️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Scikit-learn** — Preprocessing, KNN Regression, and evaluation
- **Pickle** — Saving the trained model
- **Streamlit** — Interactive web application
- **Git & GitHub** — Version control and project hosting

## 🔄 Project Workflow

1. **Data Loading:** Load the dataset using Pandas.
2. **Exploratory Data Analysis:** Understand the data, features, and target variable.
3. **Data Preprocessing:** Handle missing values if present and prepare the features.
4. **Encoding:** Convert categorical features into numerical representations.
5. **Feature Scaling:** Scale numerical features for distance-based learning.
6. **Train-Test Split:** Split the data into 75% training and 25% testing sets.
7. **Model Training:** Train a KNN Regressor.
8. **Model Evaluation:** Evaluate predictions using MAE, RMSE, and R² score.
9. **Model Saving:** Save the trained preprocessing and prediction pipeline using Pickle.
10. **Deployment:** Build a Streamlit app for interactive diamond price prediction.

## 🤖 Algorithm: K-Nearest Neighbors (KNN) Regression

KNN Regression predicts a numerical value by finding the nearest data points to a given input and using their target values to estimate the result.

In this project, the model learns from diamond characteristics and corresponding prices. When a user enters the details of a new diamond, the model estimates its price based on similar diamonds in the training dataset.

**Why KNN?**

- Easy to understand and implement.
- Can model relationships without assuming a fixed linear relationship.
- Uses similarities between data points to make predictions.

Feature scaling is important because KNN relies on distance calculations.

## 📊 Model Evaluation

The model is evaluated using the following metrics:

| Metric | Purpose |
|---|---|
| **MAE** | Measures the average absolute prediction error |
| **RMSE** | Gives greater weight to larger prediction errors |
| **R² Score** | Measures how well the model explains variation in diamond prices |

The actual evaluation scores should be added after running the trained model on the test dataset.

## 🌐 Streamlit Web Application

The application allows users to enter diamond characteristics and receive an estimated price.

**Application features:**
- Simple, interactive interface.
- Inputs for diamond weight and quality.
- Price prediction at the click of a button.
- Easy access through a web browser when deployed.

## 📁 Project Structure

```text
Diamond-Price-Prediction/
│
├── app.py
├── requirements.txt
├── description.txt
├── diamond_price_prediction_model.pkl
├── diamonds.csv
└── README.md
```

*Note: Keep only the files that are actually part of your project. Update the dataset filename in this structure if yours is different.*

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Diamond-Price-Prediction
```

### 3. Install the required libraries

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, follow the local URL displayed in the terminal.

## ☁️ Deployment

This application can be deployed using **Streamlit Community Cloud**.

1. Upload your project files to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select your repository and the `app.py` file.
5. Deploy the application.

Make sure `requirements.txt` includes the necessary libraries and the saved model file is available to the app.

## 💡 Learning Outcomes

Through this project, I gained practical experience in:

- Preparing data for machine learning.
- Encoding categorical variables and scaling numerical features.
- Training and evaluating a regression model.
- Saving and loading a trained model.
- Developing a machine learning web application.
- Preparing a project for GitHub and cloud deployment.

## 🔮 Future Improvements

- Compare KNN with other regression algorithms.
- Tune the number of neighbors and distance settings.
- Improve prediction accuracy through feature engineering.
- Add visualizations and model performance comparisons.
- Enhance the interface with additional charts and explanations.

## 👩‍💻 Author

**Khushi Panda**

Aspiring Data Scientist | Machine Learning Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!

**Disclaimer:** Predicted diamond prices are estimates generated by a machine learning model and may differ from actual market prices.
