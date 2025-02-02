# 🌞 Solar Power Prediction Machine Learning Model ⚡

## 📋 Project Overview

This project focuses on building a machine learning model to predict the amount of solar power generated based on various environmental and weather-related features. 🌤️ Solar power generation is influenced by factors such as the position of the sun, temperature, wind speed, sky cover, and other atmospheric conditions. By leveraging machine learning algorithms, we aim to accurately forecast solar energy production, which can help optimize energy distribution, improve grid management, and reduce reliance on fossil fuels. 🌍🌱

## 🔑 Features

The model uses the following features:

1. **distance-to-solar-noon**: ⏰
   - Represents the time difference from solar noon when the sun is at its highest point.
   - **Role**: Helps to account for variations in solar power production during different times of the day.

2. **temperature**: 🌡️
   - The air temperature at the location.
   - **Role**: Affects the efficiency of solar panels, as extreme heat or cold can reduce efficiency.

3. **wind-direction**: 🌬️
   - The direction of wind at the location.
   - **Role**: Wind direction can influence weather patterns and, indirectly, solar power generation.

4. **wind-speed**: 💨
   - The wind speed at the location.
   - **Role**: Affects weather conditions that may indirectly influence solar power output.

5. **sky-cover**: ☁️
   - The extent of cloud cover in the sky.
   - **Role**: More cloud cover reduces solar irradiance and, in turn, the amount of solar power generated.

6. **visibility**: 👀
   - The visibility at the location.
   - **Role**: Reduced visibility can indicate fog or haze, which can lower solar irradiance.

7. **humidity**: 💧
   - The level of moisture in the air.
   - **Role**: High humidity can scatter light and increase the likelihood of cloud cover, thus reducing solar power generation.

8. **average-wind-speed-(period)**: 🌪️
   - The average wind speed over a specified period.
   - **Role**: Similar to wind speed, it provides insights into weather trends that affect solar power generation.

9. **average-pressure-(period)**: 🌬️
   - The average atmospheric pressure over a specified period.
   - **Role**: Atmospheric pressure can influence weather patterns like cloud formation, which can affect solar power.

10. **power-generated**: ⚡
   - The target variable representing the amount of solar power generated.
   - **Role**: This is the variable we aim to predict.

## 🎯 Objective

The objective of this project is to predict the **power-generated** by solar panels using the listed environmental and weather-related features. By doing so, we aim to contribute to more efficient energy management and utilization of solar power resources. ☀️

## 🛠️ Approach

1. **Data Collection and Preprocessing**: The dataset is preprocessed to remove missing values, handle outliers, and normalize the features for better model performance.
   
2. **Feature Engineering**: Additional features like the time of day and atmospheric conditions are created to enhance the predictive power of the model.

3. **Model Selection and Training**: Various machine learning algorithms such as Linear Regression, Random Forest, and XGBoost are applied to predict the amount of solar power generated.

4. **Model Evaluation**: The models are evaluated using metrics like Mean Squared Error (MSE), R-squared, and other relevant performance measures to assess their predictive accuracy.

## 📈 Visualizations

- **Correlation Heatmap**: To visualize the relationships between features and power generation. 📊
- **Power vs. Wind Speed**: Scatter plot to understand the relationship between wind speed and solar power generation. 🌬️⚡

## ✅ Conclusion

By building and training a machine learning model on environmental and weather-related data, we can accurately predict solar power generation. These predictions can help optimize the energy distribution grid, improve the efficiency of solar energy utilization, and promote the transition towards renewable energy sources. 🌞💡

The final model can be deployed as an API or integrated into real-time systems to forecast solar power based on incoming environmental data. Through this approach, we can make informed decisions about energy management, reducing our dependency on non-renewable resources and supporting a more sustainable future. 🌍🌱

## 📋 Requirements

- Python 3.9 or higher
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `xgboost`, etc.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>

   pip install -r requirements.txt
   
   streamlit run dep.py
