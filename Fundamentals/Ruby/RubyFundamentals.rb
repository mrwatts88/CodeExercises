puts "Hello World!"
puts 'Hello World with single quotes'

puts 'hello' + " concatenation"

puts 'multiply me ' * 3

variable = "im a variable" # no type

puts variable 

# strings are mutable!!

puts `dir` # get outta here!! just like running the command in a cmd prompt

system("dir") # same as above, these can be used to start a separate process

myStr = "2"

puts myStr.to_i # 2

# to_s, to_f, to string and to floating point

puts variable << myStr # append to a string

str = <<end_str # << looks for the delimeter used here to know when to stop
I can type
a bunch of stuff
on multiple lines
end_str

puts str

x = 3
y = 2

x,y = y,x # swap made easy, just like in python