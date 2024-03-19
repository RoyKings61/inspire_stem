# this is a class that describes cars

class car:
   def _inti_(self,model,make,yaer_of_production,fuel_capacity,color,horse_power):
    self.model = model
    self.make = make
    self.year_of_production = yaer_of_production
    self.fuel_capacity = fuel_capacity
    self.color = color
    self.horse_power = horse_power

    def print_make(self.make):
      print("The car of {} make".format(self.make))

      my_car = car("impalla","chevrolet","1969","5500","lilac","390hp")
      other_car =car("note","nissan","2014","5100","black","380hp")
      my_car.print_make("chevrolet")

      def set_make(self,make)
        self.make = make

        def get_make(self):
          return self.make
        
        my_car.set_make("ford")
        Friends_car.set_make("toyota")

        print(my_car.get_make())
        print(Friends_car.get_make())

