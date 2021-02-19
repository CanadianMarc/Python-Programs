# Marc F.
# 02/11/2021
# MadLibs Game: Generate a random sentence based on inputted words.
...
# Setup: Picking the story and declaring variables.
import random
import colors

storynumber = random.randint(1,5)
exclamation, adverb, noun, adjective, verb = "", "", "", "", ""
# Beginning Segment - Lets them know how to start.
play = input(colors.cyan("Welcome to Marc's MadLibs game!") + "\n\nYou'll be using different words to complete a random phrase.\nAre you ready? Press any key to begin!")

# Input
while play:
  ## Grabbing the input for adverb.
  adverb = input(colors.green("\nGreat!") + "\n\nLet's get started! Give me an " + colors.blue("adverb") + "!\nHint: An adverb is a word that describes a verb! (He sings " + colors.yellow("loudly") + ").\n")
  if not adverb or not adverb.isalpha():
    print("Try again, please!")
    continue
  
  ## Grabbing the input for verb.
  verb = input("\n\nSplendid! Now give me a " + colors.blue("verb") + "!\nHint: A verb is any action word (Phillip decided to " + colors.yellow("run") + " to school today because he was running late!).\n")
  if not verb or not verb.isalpha():
    print("Try again, please!")
    continue
  
  ## Grabbing the input for noun.
  noun = input("\n\nWonderful! How about a " + colors.blue("noun") + "?\nHint: An noun is any person, place, or thing! (" + colors.yellow("Maria") + " went to the" + colors.yellow("CN Tower") + " to fire a " + colors.yellow("gun") +").\n")
  if not noun or not noun.isalpha():
    print("Try again, please!")
    continue
  
  ## Grabbing the input for exclamantion.
  exclamation = input("\n\nWonderful! How about an " + colors.blue("exclamation") + "?\nHint: An exclamation is any sudden cry or remark! (" + colors.yellow("Dang") + "! They have a test every Friday!).\n")
  if not noun or not noun.isalpha():
    print("Try again, please!")
    continue
  
  ## Grabbing the input for adjective.
  adjective = input("\n\nAbsolutely Magnificent! Lets end it off with an " + colors.blue("adjective") + "!\nHint: An adjective is a word that describes a noun! (He dog looked so " + colors.yellow("pretty") + ").\n")
  if not adjective or not adjective.isalpha():
    print("Try again, please!")
    continue
# Output (randomizing story and waiting for prompt to play again.)
  if adjective != "":
    if storynumber == 1:
      story = f"{exclamation}! He said as he ran away {adverb} from the {adjective} {noun} and hid behind a bushy tall man!"
    elif storynumber == 2:
      story = f"{exclamation}! The {noun} just {verb} {adverb} off of the {adjective} table!"
    elif storynumber == 3:
      story = f"Did you seriously forget to {verb} the project {adverb}? Marc said, as he slammed the {adjective} {noun}, screaming {exclamation}!"
    elif storynumber == 4:
      story = f"The tree fell {adverb} onto {noun}! {exclamation}! they said, as they {verb} away from the {adjective} tree!"
    else:
      story = f"{exclamation}! Jaemes said, as he realized he had 600 {adjective} {noun}s! Jaemes {verb} {adverb} in excitement!"
    print(story)
    
    play = input("\nThanks for playing!\n\nWant to play again? (Press any key to do so!)")
