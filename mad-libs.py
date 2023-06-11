# Mad Libs exercise 

# Read story from file
# Separate missing parts from static parts
# Ask for appropriate work / phrase 
# Add that to missing part 
# Update text 
# Write in file 

import sys

class StoryFull: 
    def __init__(self):
        self.__story = []

    def read_file(self): 
        with open("story.txt") as f, open("new_story.txt", "w") as new:
            full_story = f.read()
            story_list = full_story.split(" ")
            
            self.substitute_words(story_list)
            
            print(self.get_story())
            new.write(self.get_story())
            new.close()
    
    def substitute_words(self, story: list):
         for word in story: 
                if word.find(")") != -1: 
                    # Getting the prompt word from the string
                    prompt = word[word.find("(") + 1 : word.find(")")] 
                    word = self.prompt(prompt)
                    if word == "0":
                        return
                    print("+ Word added!")
                    print()
                self.__story.append(word)
    
    # Return current status of story. 
    def get_story(self):
        return " ".join(self.__story)
    
    # Function for providing the response to the prompt
    def prompt(self, prompt): 
        while True: 
            if prompt[0] in "aeoui":
                print(f"Give me an {prompt.upper()}: ")
            else: 
                print(f"Give me a {prompt.upper()}: ")
            
            print(f"{prompt.upper()} >")
            response = sys.stdin.readline().strip()
            
            if response.isspace(): 
                print("You must enter a word.")
                continue
            elif response == "0": 
                print("Closing the game. Bye!")
                return "0"
            else: 
                break
        
        return response

class MadLibsApplication: 
    def __init__(self) -> None:
        self.__story = StoryFull()
    
    def help(self):
        print()
        print(">>> Add to word from the required type!")
        print(">>> If you want to exit the game, enter zero.")
        print()
    
    def execute(self):
        self.help()
        self.__story.read_file()
        
application = MadLibsApplication()
application.execute()