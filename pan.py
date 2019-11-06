# user-defined function to check Pangram
def check_pangram(input):
   # convert input string into uppercase
   str_input = str_input.upper()

   # convert input string into Set()
   # a list of distinct elements will be formed.
   str_input = set(str_input)

# separate out alphabets from numbers and special characters
# ord(ch) returns the ASCII value of the character

dist_list = [ char for char in str_input if ord(char) in range(ord('a'), ord('z')+1)]
    if len(dist_list) == 26:
      return 'String is a Pangram'
    else:
      return 'String is not a Pangram'

# Executable main function
if __name__ == "__main__":
   str_input = input()
   print check_pangram(str_input)