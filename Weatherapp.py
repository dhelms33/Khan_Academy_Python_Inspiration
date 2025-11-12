class GhostyWeather:
    def __init__(self, name, temperature, humidity):
        self.name = name
        #self.temperature = temperature
        self.humidity = humidity
        
    
    def get_ghosty_temp(self, temperature):
        ghostly_temp_F = 0 * temperature 
        return(f"Ghosty Weather is currently {ghostly_temp_F}, ghosts cannot feel hot or cold~")
    def get_ghosty_sight(self, age):
        ghosty_eyelids = " your eyelids are never closed, it is the purest form of torture."
        if age > 16:
            return(ghosty_eyelids)
        elif age < 10:
            return("Your vision is great! You see plenty of towns and homes!")
        else:
            return(f"You can always see. ")
    
if __name__ == "__main__":
    try:
        user_input = int(input("Please input a int to see the ghostly temperature"))
        weather_instance = GhostyWeather("Dereck", 13)
        ghosty_temp = weather_instance(user_input)
        result = print(ghosty_temp)
    except ValueError as e:
            print("This is not a integer, try again!")
            