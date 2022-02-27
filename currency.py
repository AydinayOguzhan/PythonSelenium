class Currency:
    # Defining __init__ method
    def __init__(self):
        self.__name =''
        self.__purchasePrice = ''
        self.__salePrice = ''
      
    # Using @property decorator
    @property
      
    # Getter method
    def name(self):
        return self.__name
      
    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val
  
    # Deleter method
    @name.deleter
    def name(self):
       del self.__name
    
    
    @property
    def purchasePrice(self):
        return self.__purchasePrice

    @purchasePrice.setter
    def purchasePrice(self, val):
        self.__purchasePrice = val


    @purchasePrice.deleter
    def purchasePrice(self):
        del self.__purchasePrice
    
    
    
    @property
    def salePrice(self):
        return self.__salePrice

    @salePrice.setter
    def salePrice(self, val):
       self.__salePrice = val


    @salePrice.deleter
    def salePrice(self):
        del self.__salePrice
