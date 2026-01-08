def check():
    age_of_person = int(input("Enter age of Person: "))
    if age_of_person < 18:
        print("Person is  a minor")
    elif age_of_person <= 60 and age_of_person > 18:
        print("Person is adult")
    else:
        print("Person is a senior citizen")
        
def main():
    check()
    
if __name__ == "__main__":
    main()