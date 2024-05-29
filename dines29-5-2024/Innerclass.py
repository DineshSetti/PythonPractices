# class School:
#
#     def __init__(self,name,section):
#         self.name=name
#         self.section=section
#
#     class college:
#         def __init__(self,clg):
#             self.clg=clg
#
# obj=School("dinesh",3)
# obj1=School.college("giet")
# print(obj.name,obj.section,obj1.clg)

class school:
    def __init__(self,name):
        self.name=name
        self.subs=self.shop()

    def hmm(self):
        print(self.name)
        self.subs.subjects()
    class shop:
        def __init__(self):
            self.sub1="phy"
            self.sub2="chem"

        def subjects(self):
            print(self.sub1,self.sub2)

obj=school("dinesh")
obj.hmm()
