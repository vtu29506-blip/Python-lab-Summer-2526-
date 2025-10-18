def count_error_lines(filename):
    error_count = 0
    with open("log.txt","r") as file:
       for line in file:
          if "Error" in line:
              error_count+=1
              return error_count
error_lines = count_error_lines("log.txt")
print(f"Number of lines with 'Error': {error_lines}")
