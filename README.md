 Price Prediction Web App

This project is a Flask-based web application for predicting commodity prices using machine learning. It uses a Random Forest Regressor model to predict prices based on various factors such as category, commodity, unit, and currency. The web app allows users to input product details and get both a single price prediction for a specific date and a price trend over a range of dates.

Features

- **Price Prediction**: Users can input details about a product and get the predicted price for a specific date.
- **Price Trend**: Users can provide a date range, and the application will generate a price prediction trend over that range.
- **Data Visualization**: The app uses `Matplotlib` to generate and display a price prediction trend graph.
- **User-friendly Interface**: The app provides an easy-to-use web interface built with HTML forms.

 Technologies Used

- **Python**: The primary programming language used for the app.
- **Flask**: A lightweight Python web framework to create the web app.
- **Pandas**: For data manipulation and processing.
- **Scikit-learn**: For building the Random Forest Regressor model.
- **Matplotlib**: For visualizing the price trends.
- **HTML/CSS**: For building the front-end user interface.

 Setup and Installation

Prerequisites

Make sure you have the following installed:
- Python 3.x
- pip (Python's package installer)

 Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/price-prediction-web-app.git
cd price-prediction-web-app
```

Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` should contain the following dependencies:

```
Flask==2.3.2
pandas==1.5.3
scikit-learn==1.2.2
matplotlib==3.7.1
```
 Prepare the Dataset

The dataset `india new dataset.csv` should be placed in the root directory of the project. This dataset is used to train the Random Forest Regressor model. Make sure the dataset contains the relevant columns like `category`, `commodity`, `unit`, `currency`, and `price`.

Run the Flask App

Start the Flask development server by running:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`. You can open this URL in your browser to interact with the app.

How It Works

1. Data Preprocessing: 
   - The app preprocesses the dataset by encoding categorical variables (`category`, `commodity`, `unit`, `currency`) using `LabelEncoder` from scikit-learn.
   - It also extracts additional features from the `date` column, such as the `year` and `month`.

2. Model Training: 
   - A Random Forest Regressor model is trained on the dataset to predict commodity prices based on the features.

3. Prediction:
   - Users can input product details (category, commodity, unit, currency) and a date to get a single price prediction for that day.
   - Users can also input a date range, and the app will predict the price trend for that range.

4. Visualization :
   - The app generates a plot of the predicted prices over the selected date range using Matplotlib.

 Usage

Home Page: 
   - On the home page, users can select the commodity, category, unit, currency, and enter a specific date or date range to see the price prediction.
- Price Prediction : 
   - The user can input a date and product details to get a predicted price for that date.
- Price Trend :
   - The user can input a start date and end date to view the predicted price trend for that range.

Example

- Input : 
   - Category: Dairy
   - Commodity: Milk (pasteurized)
   - Unit: Liters
   - Currency: INR
   - Prediction Date: 2023-12-15
   - Start Date: 2023-01-01
   - End Date: 2023-12-31

- Output: 
   - A price prediction for the specified date.
   - A plot showing the price trend from January 1, 2023, to December 31, 2023.

 Contributions

Feel free to fork this repository and submit pull requests. Contributions are welcome!

 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 Notes:

- **Change the URL in the `git clone` command** to your actual GitHub repository URL.
- You can adjust the `requirements.txt` file as necessary to include any additional packages you use in your project.
- Ensure that the dataset (`india new dataset.csv`) and any other relevant files are included or properly referenced in your repository.

