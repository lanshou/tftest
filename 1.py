#!/usr/bin/python

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./mnist/", one_hot=True)
print mnist.train.num_examples
