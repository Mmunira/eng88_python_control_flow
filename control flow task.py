# # Movie Ratings
# # As a user I should be able to ask the user for the rating, and recieve back the appropriate response:

film_rating = [
    'universal -> everyone can watch.',
    'pg --> General viewing, but some scenes may be unsuitable for young children.',
    '12 --> Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.',
    '15 --> No one younger than 15 may see a 15 film in a cinema.',
    '18 --> No one younger than 18 may see an 18 film in a cinema.'
]

age = input("enter your age")
if int(age) >= 18:
      print("you can watch all films")
elif int(age) >= 15:
    print("you can watch rating films 15, 12, pg, or U")
elif int(age) >= 12:
    print("you can watch rating films 12, pg or U")
elif int(age) <= 12:
    print("you can watch 12 or pg rating films")
elif int(age) <= "pg":
    print("you can  watch pg or U rating films")

for exit_code in age:
    if exit_code == "exit":
        break


