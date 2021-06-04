class Car(object):
    def _init_(self,model,color):
        self.color=color
        self.model=model

    def start(self):
        print('car started moving')

    def stop(self):
        print('car stoped')

bmw=Car()
bmw.color='Black'
print(bmw.color)
