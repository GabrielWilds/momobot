import random


class Numberguesser:
    """
    Generates a random number, asks the users to guess it, with three chances given.
    """
    
    random_number = 0
    guess_count = 0
    game_active = False
    numer = False
    first_number = 0
    second_numer = 0
    second_stat = 'low'
    
    def __init__(self, bot):
        self.bot = bot
        bot.register_command('numberguesser', self.number_guesser)
        bot.register_command('numerguesser', self.numer_guesser)
        
    def number_guesser(self, data):
        if self.game_active == False:
            self.random_number = random.randint(1,10)
            self.game_active = True
            self.guess_count = 3
            self.bot.register_command('guess', self.guess)
            self.bot.register_command('quit', self.quit)
            self.bot.say("Number Guesser. We have generated a number between 1 and 10. Guess the right value.", data['channel'])
            self.bot.say("Say !guess [number] to make a guess. You have three guesses.", data['channel'])    
        else:
            self.bot.say("There is currently a game active. Either finish that game, or quit the session with !quit", data['channel'])
            
    def numer_guesser(self, data):
        if self.game_active == False:
            self.numer = True
            self.game_active = True
            self.guess_count = 3
            self.bot.register_command('guess', self.numer_guess)
            self.bot.register_command('quit', self.quit)
            self.bot.say("Number Guesser. We have generated a number between 1 and 10. Guess the right value.", data['channel'])
            self.bot.say("Say !guess [number] to make a guess. You have three guesses.", data['channel'])    
        else:
            self.bot.register_command('quit', self.quit)
            self.bot.say("There is currently a game active. Either finish that game, or quit the session with !quit", data['channel'])
      
    def guess(self, data):
        if not data['message'].isdigit():
            print "bad input"
            self.bot.say("Incorrect input. Guess only numbers from 1 to 10.", data['channel'])
        else:
            print "good input, checking..."
            self.guess_count = self.guess_count - 1
            if int(data['message']) == self.random_number:
                self.bot.say("You win, " + data['username'] + "! Your guess of " + str(self.random_number) + " was right!", data['channel'])
                self.game_active = False
                self.bot.unregister_command('quit')
                self.bot.unregister_command('guess')
            elif int(data['message']) > self.random_number:
                self.bot.say("Your guess is too high.", data['channel'])
                if self.guess_count > 0:
                    self.bot.say("Guess again. You have " + str(self.guess_count) + " guesses remaining.", data['channel'])
                elif self.guess_count == 1:
                    self.bot.say("Guess again. You have 1 final guess remaining.", data['channel'])
                else:
                    self.bot.say("You've ran out of guesses! :( Game Over. The number was " + str(self.random_number) + ".", data['channel'])
                    game_active = False
                    self.bot.unregister_command('quit')
                    self.bot.unregister_command('guess')
            elif int(data['message']) < self.random_number:
                self.bot.say("Your guess is too low.", data['channel'])
                if self.guess_count > 1:
                    self.bot.say("Guess again. You have " + str(self.guess_count) + " guesses remaining.", data['channel'])
                elif self.guess_count == 1:
                    self.bot.say("Guess again. You have 1 final guess remaining.", data['channel'])
                else:
                    self.bot.say("You've ran out of guesses! :( Game Over. The number was " + str(self.random_number) + ".", data['channel'])
                    self.game_active = False
                    self.bot.unregister_command('quit')
                    self.bot.unregister_command('guess')
    
    def numer_guess(self, data):
        print "numer guess made"
        if not data['message'].isdigit():
            self.bot.say("Incorrect input. Guess only numbers from 1 to 10.", data['channel'])
        else:
            if self.guess_count == 3:
                self.first_numer = int(data['message'])
                if self.first_numer < 5:
                    self.bot.say("Your guess of " + str(self.first_numer) + " is too low.", data['channel'])
                    self.guess_count = self.guess_count - 1
                    self.bot.say("Guess again. You have " + str(self.guess_count) + " guesses remaining.", data['channel'])
                else:
                    self.bot.say("Your guess of " + str(self.first_numer) + " is too high.", data['channel'])
                    self.guess_count = self.guess_count - 1
                    self.bot.say("Guess again. You have " + str(self.guess_count) + " guesses remaining.", data['channel'])
            elif self.guess_count == 2:
                self.second_numer = int(data['message'])
                if self.first_number < 5:
                    if self.second_numer < 3:
                        self.bot.say("Your guess is too low.", data['channel'])
                        self.second_stat = 'low'
                        self.guess_count = self.guess_count - 1
                        self.bot.say("Guess again. You have 1 final guess remaining.", data['channel'])
                    else:
                        self.bot.say("Your guess is too high.", data['channel'])
                        self.second_stat = 'high'
                        self.guess_count = self.guess_count - 1
                        self.bot.say("Guess again. You have 1 final guess remaining.", data['channel'])
                else:
                    if self.second_numer < 8:
                        self.bot.say("Your guess is too low.", data['channel'])
                        self.second_stat = 'low'
                        self.guess_count = self.guess_count - 1
                        self.bot.say("Guess again. You have 1 final guess remaining.", data['channel'])
                    else:
                        self.bot.say("Your guess is too high.", data['channel'])
                        self.second_stat = 'high'
                        self.guess_count = self.guess_count - 1
                        self.bot.say("Guess again. You have 1 final guess remaining.", data['channel'])
            else:
                self.numer = False
                self.game_active = False
                self.bot.unregister_command('quit')
                self.bot.unregister_command('guess')
                if self.first_number < 5:
                    while True:
                        number = random.randint(self.first_number + 1, 11)
                        if number in [self.first_numer, self.second_numer, int(data["message"])]:
                            pass
                        else:
                            break
                    self.bot.say("You've ran out of guesses! :( Game Over. The number was " + str(number) + ".", data['channel'])
                else:
                    while True:
                        number = random.randint(1, self.first_number - 1)
                        if number in [self.first_numer, self.second_numer, int(data["message"])]:
                            pass
                        else:
                            break
                    self.bot.say("You've ran out of guesses! :( Game Over. The number was " + str(number) + ".", data['channel'])
                
        
    def quit(self, data):
        if self.game_active == True:
            self.bot.say("Game Session Ended. The random number was " + str(self.random_number), data['channel'])
            self.game_active = False
            self.numer = False
            self.bot.unregister_command('quit')
            self.bot.unregister_command('guess')
        else:
            self.bot.say("No game active to quit. Say !numberguesser to start a new game.", data['channel'])