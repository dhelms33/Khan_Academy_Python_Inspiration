class UrlPaths(KhanAcademy):
    def __init__(self, language_code, subject):
        self.language_code = language_code
        self.subject = subject

    def make_url(self.language_code, self.subject):
        url = "https://" + self.language_code + ".KhanAcademy.org/" + self.subject 
        return url 