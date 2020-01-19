#!/usr/bin/env python3

import tensorflow as tf
import ee

# Testing tensorflow
tf.compat.v1.disable_eager_execution()
hello = tf.constant('Hello, TensorFlow!')
sess = tf.compat.v1.Session()
print(sess.run(hello))

# Testing Earth Engine
# Initialize the Earth Engine module.
ee.Initialize()
# Print metadata for a DEM dataset.
print(ee.Image('USGS/SRTMGL1_003').getInfo())