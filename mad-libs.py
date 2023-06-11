# MAD LIBS EXERCISE
import sys

class StoryFull: 
    def __init__(self):
        self.__story = []
        
    def execute(self): 
        self.read_file()
        self.substitute_words()
        self.write_file()
        print(self.get_story())
        
    # Read the source story file
    def read_file(self): 
        with open("story.txt") as f:
            self.__story = f.read().split(" ")
    
    # Write the new story in a separate file
    def write_file(self):
        with open("new_story.txt", "w") as new_f:
            new_f.write(self.get_story())
            new_f.close()
        
    # Return current status of story. 
    def get_story(self):
        if self.substitute_words() == "0":
            print("Closing the game. Bye!")
            return None
        else: 
            return " ".join(self.__story)
    
    def substitute_words(self):
        for i in range(len(self.__story)): 
            word = self.__story[i]
            if word.find("(") != -1: 
                # Getting the prompt word from the string
                prompt = word[word.find("(") + 1 : word.find(")")] 
                new_word = self.prompt(prompt) + word[word.find(")") + 1:]
                
                # Check if the user wanted to quit the fame and if not, append the word to the sentence
                if new_word == "0":
                    return "0"
                self.__story[i] = new_word
                print("+ Word added!")
                print()
        return self.__story
    
    # Function for providing the response to the prompt
    def prompt(self, prompt): 
        while True: 
            # Need to check whether to use A or AN
            if prompt[0] in "aeoui": 
                print(f"Give me an {prompt.upper()}: ")
            else: 
                print(f"Give me a {prompt.upper()}: ")
            
            # PROMPT input
            print(f"{prompt.upper()} >")
            response = sys.stdin.readline().strip()
            
            # PROMPT test
            if response.isspace(): 
                print("You must enter a word.")
                continue
            else: break
            
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
        self.__story.execute()
        
application = MadLibsApplication()
application.execute()