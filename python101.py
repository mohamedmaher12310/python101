numbersToNames={
    '1111111111':'Amal',
    '2222222222':'Mohammed',
    '3333333333':'Khadijah',
    '4444444444':'Abdullah',
    '5555555555':'Rawan',
    '6666666666':'Faisal',
    '7777777777':'Layla'
}


def check_number(number):
    length = len(number)
    if length != 10:
        print("This is invalid number")
        return False
    else:
        for iter in number:
            if '0'<=iter<='9':
                pass
            else:
                print("This is invalid number")
                return False

    return True


def search_by_number(number):
    num_found_flag=0
    if check_number(number):
        for num in numbersToNames:
            if num == number:
                num_found_flag=1
                print(numbersToNames[num])
                return numbersToNames[num]
        if num_found_flag !=1 :
            print("Sorry, the number is not found")


my_num = input("Please enter number to search:")

search_by_number(my_num)

