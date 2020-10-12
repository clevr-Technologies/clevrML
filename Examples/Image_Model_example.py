'''
The following example demostrates how to build an Image Classification model, run a prediction and make an edit. 
The example will create an Image classifier that is able to recognize a stop sign and a yield sign.

Please Note: 
- You must source your own data for this tutorial.
- You must have a clevrML Developer Account with an API Key and have set up a budget. For more, see www.clevrML.com/sdk-docs
'''

from clevrml import Image_Model
import os

# Recommended 
key = os.environ['my-api-key']
# Unsecure
key = 'API-KEY-123'

model = Image_Model()


# Build a stop sign and yield sign recognizer. Please note, you must replace the example_folders argument with a list of your directories containing model data.
model.build_model(
  api_key=key,
  class_names=['Stop-Sign', 'Yield-Sign'],
  example_folders=['/tmp/stop_sign_examples/', '/tmp/yield_sign_examples/'],
  model_name='Traffic-Sign-Classifier' 
)


# Make a prediction. Make sure to change the image_file_path argument with the path to your inference image.
model.predict(
  api_key=key,
  image_file_path='/path/yield_sign_test.jpg',
  model_name='Traffic-Sign-Classifier'
)
