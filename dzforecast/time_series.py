import statistics
import numpy as np

class TimeSeriesForecast(list):
    """
    A class that inherits from a list and provides a forecast method
    based on the simple mean of the historical data.
    """
    def __init__(self, data, data_type='list'):
        """
        Initializes the TimeSeriesForecast object with an array-like data.

        Args:
            data: An iterable (e.g., list, tuple) of numeric data points.
            data_type: Can be either list or numpy
        """
        if data_type == 'list':
            super().__init__(data)  # Initialize the list base class
        elif data_type == 'numpy':
           super().__init__(list(data)) #convert the numpy to list and initialize the list base class
        else:
          raise ValueError("data_type should be either 'list' or 'numpy' ")

    def forecast(self, future_points, method="mean"):
       """
       Calculates a forecast for a given number of future points using the mean of historical data.

       Args:
           future_points: The number of future time points to forecast.

       Returns:
            A list containing the forecast values. The length of the
           list is equal to future_points.
       """
       if not self:
         return [None] * future_points # Handle empty list, return list of None values
       if future_points < 0:
         raise ValueError("future_points should be greater than or equal to 0.")

       if method == "mean":
          mean = statistics.mean(self)
          return [mean] * future_points
       else:
          raise ValueError("Method is not available")

    def add_data(self, new_data):
      """
      Adds new data to the time series

      Args:
          new_data: The data that needs to be added
      """
      if isinstance(new_data, list):
          self.extend(new_data)
      elif isinstance(new_data,(int, float)):
          self.append(new_data)
      else:
        raise ValueError("The provided data should be a list, int or float")
    
    def get_lambda_coef(series):
        x=[series[i] for i in range(len(series))]
        for i in range(len(x)-1):
            for j in range(len(x)-1):
                if x[j]>=x[j+1]:
                    z=x[j]
                    x[j]=x[j+1]
                    x[j+1]=z
        i=[j for j in range(1,len(x)+1)]
        f=[(i[j]-0.375)/(len(x)+0.25) for j in range(len(x))]
        u=[norm.ppf(f[i]) for i in range(len(x))]
            
        lambda_coef=0
        width=3
        step=width/6
        k=lambda_coef-width
        iteration=1
        while iteration<=15:
            r_vector=[]
            lambda_vect=[]
            while k<=lambda_coef+width:
                if k==0:
                    y=[np.log(i) for i in x]
                else:
                    y=[(i**k-1)/k for i in x]
                r_vector.append(pearsonr(y, u)[0])
                k+=step
            k=lambda_coef-width
            while k<=lambda_coef+width:
                lambda_vect.append(k)
                k+=step
            lambda_coef=lambda_vect[r_vector.index(max(r_vector))]
            width/=2
            step/=3
            k=lambda_coef-width
            iteration+=1
        return lambda_coef

if __name__ == '__main__':
    # Example usage
    data = [10, 12, 15, 13, 16, 18, 17]
    ts = TimeSeriesForecast(data)
    print(f"Original data: {ts}")

    forecast_steps = 3
    forecast = ts.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points using mean: {forecast}")

    forecast_steps = 5
    forecast = ts.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points using mean: {forecast}")

    # Example with an empty dataset
    ts_empty = TimeSeriesForecast([])
    forecast_steps = 2
    forecast = ts_empty.forecast(forecast_steps)
    print(f"Forecast for empty dataset for {forecast_steps} points: {forecast}")


    # Example Usage with numpy array
    data_np = np.array([20, 22, 25, 23, 26, 28, 27])
    ts_np = TimeSeriesForecast(data_np, data_type='numpy')
    print(f"Original data (numpy): {ts_np}")

    forecast_steps = 4
    forecast_np = ts_np.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points from numpy data: {forecast_np}")

    ts_np.add_data(29)
    print(f"New data is added: {ts_np}")
    ts_np.add_data([30,31,32])
    print(f"New data is added: {ts_np}")
