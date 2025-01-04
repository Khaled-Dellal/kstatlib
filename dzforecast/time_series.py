import statistics

class TimeSeriesForecast(list):  # Inheriting from 'list'
    """
    A class that inherits from a list and provides a forecast method
    based on the simple mean of the historical data.
    """
    def __init__(self, data):
        """
        Initializes the TimeSeriesForecast object with an array-like data.

        Args:
            data: An iterable (e.g., list, tuple) of numeric data points.
        """
        super().__init__(data)  # Initialize the list base class

    def forecast(self, future_points):
        """
        Calculates a forecast for a given number of future points using the mean of historical data.

        Args:
            future_points: The number of future time points to forecast.

        Returns:
            A list containing the forecast values. The length of the
            list is equal to future_points.
        """
        if not self:
            return [None] * future_points  # Handle empty list, return list of None values

        mean = statistics.mean(self)
        return [mean] * future_points

if __name__ == '__main__':
    # Example usage
    data = [10, 12, 15, 13, 16, 18, 17]
    ts = TimeSeriesForecast(data)

    print(f"Original data: {ts}")

    forecast_steps = 3
    forecast = ts.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points: {forecast}")

    forecast_steps = 5
    forecast = ts.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points: {forecast}")

    # Example with an empty dataset
    ts_empty = TimeSeriesForecast([])
    forecast_steps = 2
    forecast = ts_empty.forecast(forecast_steps)
    print(f"Forecast for empty dataset for {forecast_steps} points: {forecast}")
