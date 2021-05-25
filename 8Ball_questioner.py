import random

name = input("Whats your name\n >>")

question = input("Write the yes or no question that you want the 8-ball answer for you\n >>")
answer = {
  1:"Yes - definitely.",
  2:"It is decidedly so.",
  3:"Without a doubt.",
  4:"Reply hazy, try again.",
  5:"Ask again later.",
  6:"Better not tell you now.",
  7:"My sources say no.",
  8:"Outlook not so good.",
  9:"Very doubtful."
}
random_number = random.randint(1,9)
print(name, "your question was ", question, "and the 8-Ball says \n", answer.get(random_number))