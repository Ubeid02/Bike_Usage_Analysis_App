# Bike Sharing Data Dashboard

This project is a Bike Sharing Dashboard built using Streamlit to explore the bike-sharing dataset. The dashboard provides insights into bike rentals on weekdays vs weekends, bike rentals per hour, and an RFM (Recency, Frequency) analysis based on bike usage.

## Features

- **Bike Rentals: Weekday vs Weekend**: Analyze the total bike rentals on weekdays compared to weekends.
- **Bike Rentals per Hour**: Visualize bike rentals for each hour of the day.
- **RFM Analysis**: Provides insights into user behavior by analyzing the recency and frequency of bike rentals, segmented by user type (casual or registered).

## How to Run

1. **Download  the dataset**: You can download the bike-sharing dataset.
    ```bash
    https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view
    ```

2. **Install dependencies**:
    Ensure you have Python 3 installed. Install required packages using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application**:
    After installing the dependencies, run the following command to start the dashboard:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

4. **Access the Dashboard**:
    Once Streamlit is running, you can view the dashboard in your web browser by navigating to `http://localhost:8501/`.

## Dataset

The dataset used in this project is a combination of daily and hourly bike rental data, including:
- Rental counts
- Weather conditions
- User type (casual or registered)
- Day, hour, season, and more.

The dataset is cleaned and combined into a single file: `combined_bike_sharing_data.csv`.

## Project Structure

- `dashboard.py`: The main Streamlit app file that contains the dashboard code.
- `combined_bike_sharing_data.csv`: The cleaned dataset used for analysis.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies required to run the project.

## Dependencies

The project uses the following libraries:
- **pandas**: For data manipulation and analysis.
- **seaborn**: For advanced visualizations.
- **matplotlib**: For plotting graphs.
- **streamlit**: To create the interactive dashboard.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

