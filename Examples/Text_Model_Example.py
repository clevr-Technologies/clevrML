'''
The following example demostrates how to build an Text Classification model, run a prediction and make an edit using the clevrML Python SDK. 
The example will create an Text Classifier that is able to predict whether a restaurant review is Negative or Positive.

Please Note: 
- You must source your own data for this tutorial.
- You must have a clevrML Developer Account with an API Key and have set up a budget. For more, see www.clevrML.com/sdk-docs
- Please Note: The data to build your Text Classifier must be a .txt file and must be in the following format:

class1,example
class1,example
class2,example,
class2,example
....
'''

from clevrml import Text_Model
import os

# Recommended 
key = os.environ['my-api-key']
# Unsecure
key = 'API-KEY-123'

model = Text_Model()

# Build a text classification model for restaurant reviews. Please note, you must change the references_path argument to the path that contains the data for your models "Memory".
model.build_model(
  api_key=key,
  references_path='/tmp/restaurant_examples.txt',
  model_name="review-classifier"
)



# Run a prediction on the restaurant review classifier.
model.predict(
  api_key=key,
  input_sentence="The food and the service was awesome!",
  model_name="review-classifier"
)




# Make an edit to the review-classifier model by adding new reviews to both classes.
model.edit_model(
  api_key=key,
  references_path='/tmp/NEW_restaurant_example.txt',
  model_name='review-classifier'
)
