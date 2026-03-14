class contract:
    def __init__(self, caterer, client, parties):
        self.caterer = caterer
        self.client = client 
        self.parties = parties
    def create_contract(self.caterer, self.client):
        client = input("Input your client ")
        caterer = input("Input your caterer: ")
        contract = (
            "This catering contracted is between "
            + self.caterer + " " + self.client
        )
        return contract
    
    def rounded_responses(response_num):
        rounded_response = round(rounded_num, 3)
        return rounded_response
    
    def convert_responses(response_num_rounded):
        converted_response = bool(rounded_responses(response_num_rounded))
        return("Converted ranking to are you satisfied False = No, True = YES", converted_response)
    
    def servings_vs_spices(servings):
        spices = servings * (6*2)/3
        values = max(servings) + min(spices)
        return values
    
    
        