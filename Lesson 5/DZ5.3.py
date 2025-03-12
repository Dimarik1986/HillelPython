import string
my_string = ("i like python community! Should, I. subscribe? Yes! Should, I. subscribe? Yes! Should, I. subscribe? Yes!:"
             " Python Community Python Community I. subscribe? Yes! Should, I. subscribe? Yes! Python Community Python Community")
# my_string = "Should, I. subscribe? Yes!"
# my_string = "Python Community"
# my_string = "i like python community!"

my_string = my_string.title().replace(" ","")

for y in range(len(string.punctuation)):
    my_string = my_string.replace(string.punctuation[y], "")

print("#"+my_string[:140])
