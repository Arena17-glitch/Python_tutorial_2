def countListElements(lst):
    output = {}
    for val in lst:
        if val in output:
            output[val] = output[val] + 1
        else:
            output[val] = 1
    return output

def main():
    input1 = [1,2,2,3,3,3]
    input2 = [4,1,6,5,4,5,5,1,4]
    result = countListElements(input2)
    print(result)

if __name__ == "__main__":
    main()