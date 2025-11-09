class Company:
    job = "developer"
    def __init__(self,lang="python"):
        self.lang = lang
        print("default constructor called language = ",self.lang)
emp = Company()
emp1 = Company("java")
print("he is a",Company.job,"and he is using ",emp1.lang)
