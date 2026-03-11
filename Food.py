class Food:
    def __init__(self, servings):
       self.servings = servings
       
    def get_servings(self.serving):
        servings=int(self.serving)
         servings += 2
        return(servings, "increased by two because at Granny's.")

if __name__ == "__main__":
    class_obj = Food(2)
    result = class_obj.get_servings(int(input("Please input serving size: ")))