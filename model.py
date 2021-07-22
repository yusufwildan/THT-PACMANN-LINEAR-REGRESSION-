class LinearReg:

  #INPUT
  def __init__(self):
      self.data_x = []
      self.data_y = []
      self.data_x2 = []
      self.data_y2 = []
      self.coef = 0
      self.intercept = 0
      self.MSE = 0
      self.Coefdet = 0

  #LINEAR REGRESSION FUNCTION    
  def fit(self, data_x, data_y):
      self.data_x = data_x
      self.data_y = data_y
      
      sumx=0;sumy=0;sumxy=0;sumx2=0

      n = len(data_x)
        
      #sum of x
      for i in range (0,n):
          sumx = sumx + data_x[i]
            
      #sum of y
      for i in range (0,n):
          sumy = sumy + data_y[i]
        
      #sum of xy
      for i in range (0,n):
          sumxy = sumxy + data_x[i]*data_y[i]
        
      #sum of square of x
      for i in range (0,n):
          sumx2 = sumx2 + data_x[i]**2
        
      avgx = sumx/n # average of x
      avgy = sumy/n # average of y
        
      m= (n*sumxy - sumx*sumy)/(n*sumx2 - sumx**2)
      c= avgy - m*avgx
        
      st = 0; sr=0
      for i in range (0,n):
          st = st + (data_y[i]-avgy)**2
          sr = sr + (data_y[i]-m*data_x[i]-c)**2
        
      MSE = (sr/n) # Mean squared error
      Coefdet = (st-sr)/st # Coefficient of determination
      
      self.coef = m
      self.intercept = c
      self.MSE = MSE
      self.Coefdet = Coefdet

  #PREDICT DATA BASED ON REGRESSION FUNCTION ABOVE    
  def predict(self, data_x2):
      self.data_x2 = data_x2
      n = len(data_x2)
      data_y2 = [0 for i in range (0,n)]
      for i in range (0,n):
        data_y2[i] = self.coef*data_x2[i] + self.intercept
        print (data_y2[i])
      