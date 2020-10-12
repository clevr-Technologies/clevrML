'''
The following example demostrates how to build a Forecasting model, run a prediction and make an edit. 
The example will create a Model that will Forecasting the amount of sales for the day based off the amount 
of customers who come in to a 'store'.

Please Note: 
- You must source your own data for this tutorial.
- You must have a clevrML Developer Account with an API Key and have set up a budget. For more, see www.clevrML.com/sdk-docs
- The data must be in a .csv format, and follow the same format:

Customers | Sales
val1      | val1
val2      | val2
...       | ...

'''

from clevrml import Forecasting_Model
import os

# Recommended 
key = os.environ['my-api-key']
# Unsecure
key = 'API-KEY-123'

model = Forecasting_Model()

# Build a Forecasting model, where sales WILL be dependent on how many customers come in for a day. Note: You must change the reference_path argument to your own path.
model.build_model(
  api_key=key,
  independent="customers",
  dependent="sales",
  reference_path='/tmp/customer_sales_data.csv',
  model_name="Sales_Forecast_Model"
)

# With this prediction, we want to see how much sales we will make if 103 customers come in on a given day. Note that for any model, the input_value argument must be a float or integer
model.predict(
  api_key=key,
  input_value=103,
  model_name="Sales_Forecast_Model"
)


# Make an edit to an existing Forecasting Model. In this case, we will add more to our models "Memory" that will consit of more Sales/Customer data points.
model.edit_model(
  api_key=key,
  independent="customers",
  dependent="sales",
  reference_path='/tmp/NEW_customer_sales_data.csv',
  model_name="Sales_Forecast_Model"
)

