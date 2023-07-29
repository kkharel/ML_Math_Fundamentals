class Metrics():
  
  def euclidean_distance(self, X, Y):
    distance = 0
    for i in range(min([len(X), len(Y)])):
      distance += (X[i] - Y[i])**2
    return distance**0.5
  # 
  # def euclidean_distance2(self, X, Y):
  #   
  #   distance = (sum([(x-y)**2 for x,y in zip(X,Y)]))**0.5
  #   return distance
  
  def manhattan_distance(self, X, Y):
    distance = 0
    for i in range(min([len(X), len(Y)])):
      distance += abs(X[i] - Y[i])
    return distance
  
  # def manhattan_distance2(self, X, Y):
  #   distance = sum([abs(i-j) for i,j in zip(X,Y)])
  #   return distance
  
  def cosine_similarity(self, X, Y):
    numerator = sum(i*j for i,j in zip(X,Y))
    denominator = ((sum([i**2 for i in X]))**0.5)*((sum([j**2 for j in Y]))**0.5)
    return numerator/float(denominator)
  
  def jaccard_similarity(self, X, Y):
    jac_sim = len(set(X).intersection(Y))/len(set(X).union(Y))
    return jac_sim
    
  
def distances_and_similarities(X,Y):
  metrics = Metrics()
  return [metrics.euclidean_distance(X,Y),
          metrics.manhattan_distance(X,Y),
          metrics.cosine_similarity(X,Y),
          metrics.jaccard_similarity(X,Y)]
            
X = [1,2,3,4,5,6]
Y = [6,7,8,9,10,11]
  
distances_and_similarities(X,Y)
    
