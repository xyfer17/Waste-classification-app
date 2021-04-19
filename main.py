import numpy as np
from tensorflow.keras.preprocessing import image
import tensorflow as tf

def predictions(filename):

  model=tf.keras.models.load_model("model/waste.h5")

  test_image = image.load_img('uploads/'+filename,target_size = (64, 64))
  test_image = image.img_to_array(test_image)
  test_image = test_image = np.expand_dims(test_image, axis = 0)
  result = model.predict(test_image)
  prediction = ''
  if result[0][0] == 1:
    prediction = 'recyclable waste'
  else:
    prediction = 'organic waste'
  return prediction

