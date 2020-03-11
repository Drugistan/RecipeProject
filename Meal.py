class Recipe:
	def __init__(self, recipeName):
		self.__recipeName = recipeName
		self.Ingredients = () 
		self.Instruction = ""



class Food:
	def __init__(self, foodName):
		self.__foodName = foodName
		self.vitamins = {
                   
                   "vitamin A" : 0,
                   "vitamin D" : 0,
                   "vitamin E" : 0,
                   "vitamin K" : 0,
                   "vitamin C" : 0,
                   "vitamin B1": 0,
                   "vitamin B2": 0,
                   "vitamin B3": 0,
                   "vitamin B4": 0,
                   "vitamin B5": 0,
                   "vitamin B6": 0,
                   "vitamin B7": 0,
                   "vitamin B8": 0
		}

		self.Minerals = {

                   "Calcium"   :0,
                   "Phosphorus":0,
                   "Potassium": 0,
                   "Magnesium": 0,
                   "Salt"     : 0,
                   "Iron"     : 0,
                   "Zinc"     : 0,
                   "Copper"   : 0,
                   "Chromium" : 0,
		}