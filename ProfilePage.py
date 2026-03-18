class ProfilePage:
    """ """
    def __init__(self, first_name: str, age: int, job: str):
        self.first_name: str = first_name
        self.age: int = age
        self.job: str = job
    
    def profile_data(self, first_name: str) -> str:
        return(f"<h1>Hello {self.first_name} you have a wonderful name</h1>")