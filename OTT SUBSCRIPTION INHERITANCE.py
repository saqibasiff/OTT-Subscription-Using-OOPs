class OTTSubscription:
    def Plan(self):
        self.id = int(input("\nEnter Your ID = "))
        self.name = str(input("Enter You Name = "))
        self.plan = str(input("Enter Your Subscription Plan ( Monthly \ Yearly ) = "))

    def Subscribe(self):
        print(f" User Named '{self.name}' Just Subscribed The '{self.plan}' Plan")

    def Unsubscribe(self):
        print(f" User Named '{self.name}' Just Unsubscribed The '{self.plan}' Plan")

subscription = OTTSubscription()

class PremiumSubscription(OTTSubscription):
    def Plan(self):
        self.id = int(input("\nEnter Your ID = "))
        self.name = str(input("Enter You Name = "))
        self.plan = str(input("Enter Your Subscription Plan ( Monthly \ Yearly ) = "))
        self.screen = int(input("How Much Screens Do You Want (1 - 5) = "))

    def Subscribe(self):
        print(f'''                   User Named '{self.name}'
                   Subscriber Status = Subscribed
                   Usage Plan = '{self.plan}' Plan
                   Screens = {self.screen} ''')
        
premium = PremiumSubscription()

print('''What Do You Want To Do?
         1. Subscribe 
         2. Unsubscribe''')

choice = int(input("Enter Your Choice = "))

if choice == 1:
    premium.Plan()
    premium.Subscribe()

elif choice == 2:
    subscription.Plan()
    subscription.Unsubscribe()
