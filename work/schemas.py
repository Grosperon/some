from pydantic import BaseModel

class Tee(BaseModel):
    type_of_fermentation: str
    portions: int
       
    def tea_party(self):
        self.portions -= 1
        print("После чайной паузы в запасе осталось", self.portions, "порций чая с этикеткой", self.type_of_fermentation)