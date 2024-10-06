# Bike Sharing Data Dashboard

This project is a Bike Sharing Dashboard built using Streamlit to explore the bike-sharing dataset. The dashboard provides insights into bike rentals on weekdays vs weekends, bike rentals per hour, and an RFM (Recency, Frequency) analysis based on bike usage.

## Features

- **Bike Rentals: Weekday vs Weekend**: Analyze the total bike rentals on weekdays compared to weekends.
- **Bike Rentals per Hour**: Visualize bike rentals for each hour of the day.
- **RFM Analysis**: Provides insights into user behavior by analyzing the recency and frequency of bike rentals, segmented by user type (casual or registered).

## How to Run

1. **Download the dataset**: You can download the bike-sharing dataset from the following link:
    [Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)

2. **Install dependencies**:
    Ensure you have Python 3 installed. Install required packages using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application**:
    - First, navigate to the `dashboard` directory:
    ```bash
    cd dashboard
    ```
    - Then, run the Streamlit app:
    ```bash
    streamlit run dashboard.py
    ```

4. **Access the Dashboard**:
    Once Streamlit is running, you can view the dashboard in your web browser by navigating to `http://localhost:8501/`.

## Exploratory Data Analysis (EDA)

During the EDA phase, the following aspects of the bike-sharing data are explored:

1. **Data Cleaning**: The data is cleaned by removing duplicates and handling missing values.
2. **Data Aggregation**: The dataset is aggregated to explore the total bike rentals over different time periods such as weekdays, weekends, and hours of the day.
3. **Recency and Frequency Analysis**: User behavior is explored using recency and frequency metrics to understand patterns in bike usage.

The analysis focuses on answering the following questions:
- How do bike rentals differ between weekdays and weekends?
- What is the trend of bike rentals throughout the day?
- How frequent and recent are bike rentals for casual vs. registered users?

## Dataset

The dataset used in this project is a combination of daily and hourly bike rental data, including:
- Rental counts
- Weather conditions
- User type (casual or registered)
- Day, hour, season, and more.

The dataset is cleaned and combined into a single file: `combined_bike_sharing_data.csv`.

## Project Structure

- `dashboard/dashboard.py`: The main Streamlit app file that contains the dashboard code.
- `data/combined_bike_sharing_data.csv`: The cleaned dataset used for analysis.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies required to run the project.

## Deployment

The dashboard is also deployed on Streamlit Cloud. You can view the live version of the dashboard at:

https://bikeanalysisdashboard.streamlit.app

## Dependencies

The project uses the following libraries:
- **pandas**: For data manipulation and analysis.
- **seaborn**: For advanced visualizations.
- **matplotlib**: For plotting graphs.
- **streamlit**: To create the interactive dashboard.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
