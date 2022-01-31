import numpy as np
import matplotlib.pyplot as plt
import math

class Datum:
  def __init__(self, y=None, distance=0):
    self.X = self.gen_random_XOR_inputs()
    self.distance = distance
    
    if y == "random":
      self.y = self.gen_random_output()

  def gen_random_XOR_inputs(self):
    return [np.random.uniform(0, 1), np.random.uniform(0, 1)]
  
  def gen_random_output(self):
    # in this case, we'd expect the XOR output to be 1, so we'll make 1 more likely
    if (self.X[0] > 0.5 and self.X[1] < 0.50) or (self.X[0] < 0.5 and self.X[1] > 0.50):
      if np.random.randint(0, 100) < 80:
        return 1
      return 0
    # in this other case, we'd expect the XOR output to be 0, so we'll make 0 more likely
    else:
      if np.random.randint(0, 100) < 80:
        return 0
      return 1

  def calc_distance(self, other):
    x1, y1 = self.X
    x2, y2 = other.X

    self.distance = math.sqrt((x2-x1)**2 + (y2-y1)**2) 

  def choose_using_KNN(self, data_list, k):
    label_0_count = 0
    label_1_count = 0

    for i in range(k):
      if data_list[i].y == 0:
        label_0_count += 1
      else:
        label_1_count += 1

    if label_0_count > label_1_count:
      self.y = 0
    else:
      self.y = 1
    
test_point = Datum(distance=0)  

# total number of data points
N = 10

# create the random data points
data = []
for i in range(N):
  data.append(Datum(y="random"))
  data[i].calc_distance(test_point)

# sort the data according to distance from test_point
data.sort(key=lambda x: x.distance)


# choosing a random k value for KNN
k = np.random.randint(0, N/2)

test_point.choose_using_KNN(data, k)
print(test_point.X, test_point.y)
