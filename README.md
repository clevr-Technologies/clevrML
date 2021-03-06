![Image](https://github.com/clevr-Technologies/clevrML/blob/main/clevrML%20%20%20.png)

clevrML is an End-to-End platform for creating, editing, deploying and using Machine Learning models using clevr's state-of-the-art technology Active Memory Learning (AML). With AML, you can build and deploy your Machine Learning model in as little as 10 seconds. For more information, please visit www.clevrml.com

## Table of Contents
* Install clevrML SDK
* Quickstart
* Model Types
* Official Documentation



## Install clevrML SDK
Currently, the clevrML SDK for the clevrML Developer API is only supported in Python 3, however releases in other languages are coming soon.
Language | Installation
------------ | -------------
Python 3 | `pip install clevrml`




### Quickstart

Building a model on clevrML is simple, smooth and efficient. Using the clevrML Python SDK, here is how you can build a **cat and dog Image Classification Model and automatically deploy the model:**

```python
from clevrml import Image_Model
import os

model = Image_Model()
key = os.environ['clevrml-key']    # see official clevrML docs for obtaining an API Key

model.build_model(
   api_key=key,
   class_names=["cat", "dog"],
   example_folders=["/cat_image_examples/", "/dog_image_examples/"],
   model_name="Pet-Classifier"
)
```

And getting a prediction for your model is just as simple:


```python
from clevrml import Image_Model
import os

model = Image_Model()
key = os.environ['clevrml-key']     # see official clevrML docs for obtaining an API Key

model.predict(
   api_key=key,
   image_file_path="cat_example.jpg",
   model_name="Pet-Classifier"
)
```

With Active Memory Learning, you can edit your model by simply adding new inputs to your models "Memory" to improve performance. You can add to existing classes or add new ones:


```python
from clevrml import Image_Model
import os

model = Image_Model()
key = os.environ['clevrml-key']     # see official clevrML docs for obtaining an API Key

# adding to our cat and dog classes along with creating a new "fish" class.
model.edit_model(
   api_key=key,
   class_names=["cat", "dog", "fish"],            
   example_folders=["/more_cat_images/", "/more_dog_images/", "/fish_images/"],
   model_name="Pet-Classifier"
)
```


### Model Types

clevrML currently supports the following types of custom models:

 Models 
------------ |
Image Classification 
Text Classification


### Official Documentation

Please see: https://www.clevrml.com/sdk-docs
