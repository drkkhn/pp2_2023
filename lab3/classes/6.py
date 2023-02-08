class filterprint() :
    def IsPrime(self , n):
        if n < 2 :
            return False 
        else :
            for i in range(2,n):
                if (n % i == 0):
                    return False 
        return True 
    
    def filter(self,ListOfNumbers):
        return filter(lambda a : self.IsPrime(a),ListOfNumbers)
ListOfNumbers = [1,2,3,4,5,6,7,8,9,10]
filter_prime = filterprint()
PrimeNumbers = list(filter_prime.filter(ListOfNumbers))
print(PrimeNumbers)

        