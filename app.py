from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import datetime
import matplotlib.pyplot as plt
import io
import base64

# Initialize the Flask app
app = Flask(__name__)

# Step 1: Load the dataset
file_path = 'india new dataset.csv'
data = pd.read_csv(file_path)

# Step 2: Preprocess the data
# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y')

# Encode categorical features
label_encoders = {}
for column in ['category', 'commodity', 'unit', 'currency']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Extract additional features from the date column
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

# Drop unnecessary columns
data_cleaned = data.drop(columns=['date', 'usdprice'])

# Define features (X) and target (y)
X = data_cleaned.drop(columns=['price'])
y = data_cleaned['price']

# Train the Random Forest model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(X_train, y_train)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user inputs
        category_input = request.form['category']
        commodity_input = request.form['commodity']
        unit_input = request.form['unit']
        currency_input = request.form['currency']
        prediction_date = request.form['prediction_date']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        # Encode inputs
        category_encoded = label_encoders['category'].transform([category_input])[0]
        commodity_encoded = label_encoders['commodity'].transform([commodity_input])[0]
        unit_encoded = label_encoders['unit'].transform([unit_input])[0]
        currency_encoded = label_encoders['currency'].transform([currency_input])[0]

        # Predict the price for a specific date
        desired_date_obj = datetime.datetime.strptime(prediction_date, '%Y-%m-%d')
        specific_product = {
            'category': category_encoded,
            'commodity': commodity_encoded,
            'unit': unit_encoded,
            'currency': currency_encoded,
            'year': desired_date_obj.year,
            'month': desired_date_obj.month
        }
        specific_product_df = pd.DataFrame([specific_product])
        specific_price = model.predict(specific_product_df)[0]

        # Generate a range of dates for the trend
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        date_range = pd.date_range(start=start_date_obj, end=end_date_obj, freq='MS')

        # Predict prices for the date range
        predicted_prices = []
        for date in date_range:
            product_details = {
                'category': category_encoded,
                'commodity': commodity_encoded,
                'unit': unit_encoded,
                'currency': currency_encoded,
                'year': date.year,
                'month': date.month
            }
            product_df = pd.DataFrame([product_details])
            predicted_price = model.predict(product_df)[0]
            predicted_prices.append(predicted_price)

        # Debugging: Print predicted prices
        print("Predicted Prices:", predicted_prices)

        # Ensure there are valid predictions
        if len(predicted_prices) == 0:
            return render_template('index.html', specific_price="No predictions", plot_url=None)

        # Create a DataFrame for visualization
        prediction_df = pd.DataFrame({'Date': date_range, 'Predicted Price': predicted_prices})

        # Generate the plot
        plt.figure(figsize=(10, 6))
        plt.plot(prediction_df['Date'], prediction_df['Predicted Price'], marker='o', color='b', label='Predicted Price')
        plt.title(f"Price Prediction Trend for {commodity_input}", fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Predicted Price', fontsize=12)
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        # Pass the result back to the template
        return render_template('index.html', specific_price=specific_price, plot_url=plot_url, options={
            key: le.classes_ for key, le in label_encoders.items()
        })

    # Pass the class labels for dropdowns to the template
    options = {
        key: le.classes_ for key, le in label_encoders.items()
    }
    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)
