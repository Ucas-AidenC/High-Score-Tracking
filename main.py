#this just makes it easier to run in vs code web, please dont delete python3 main.py

#profiles, if set already, just an example to test main at the moment
#profiles = ["jake", "joshua", "Jeramiah", "aiden"]
profiles = []

#initialising this so it can be used in a while stament later
prof_select = True

def main():
    while prof_select:
        if len(profiles) == 0:
            #wip is supposed to be adding profile func
            print("wip, is supposed to be adding profile func")
        #checking if profiles already exist
        elif len(profiles) > 0:
            #prints all profiles in order and gives the option to create one
            for i in range(len(profiles)):
                print(f"\n({i+1}) {profiles[i].capitalize()}")
                if i+1 == len(profiles):
                    print(f"\n({i+2}) New profile")
        
        try:
            selection = int(input("\nWhich profile do you want to log into?" ))
        except:
            print("wip")
main()