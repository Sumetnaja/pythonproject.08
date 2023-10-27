# OOP

class IotSAU :
    # data/property/field/attribute
    major = "SAU"
    name = ""
    
    # method (มันคือ Funciton แต่เราไม่เรียกฟังก์ชั่น)
    def showHi() :
        print('Hi....')

    def introduceMySelf(self) :
        print(f'My name is {self.major}')
        print(f'My major is {self.major}')

#-------------
# สร้าง object
obA = IotSAU( ) #เป็นการเรียกใช้ constructor ของคลาสให้ทำงาน (ถ้ามี)
obB = IotSAU( )


# การใช้งาน data ของ object คือ เอาคำมันมาใช้ หรือเปลี่ยนค่าให้มันใหม่
print( obA.major )
obA.major = "Wow"
obA.name = "ฟ้าร้อง"
obB.name = "ฝนตกแล้ว"

# การใช้งาน data ของ object คือ สั่งให้เมธอดของ object นั้นๆ ทำงาน
obA.introduceMySelf()
obB.introduceMySelf()
