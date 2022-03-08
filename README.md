# INTRO
Uses selenium to automatically solve wordle
# HOW TO USE
  to use this, download the version of chromedriver that matches your chrome version from https://chromedriver.chromium.org/
  then change  line 25, ie, driver = webdriver.Chrome('/usr/local/bin/chromedriver') to where the chrome driver is

# LOGIC

answers.py contains a class that is used to find out possible answers
get_good() gives good tries that can be used to find out other letters


# in answers.py
  check_green() checks all letters in green boxes
  
  check_yellow() checks if all the letters in yellow are in the word
  
  check_yellow_same() checks if the yellows are in the same place as the word entered into wordle, if yes it discards the word
  

# in main.py

  first required lists are initalized and selenium is imported and driver is initalized
  
  the button for each list is saved in a list
  
  the predefined word, or the word saved from last iteration is entered
  
  then the div in which entered and accepted results are displayed is taken and all divs under it are read
  
  this reading is then saved in arrays and this data is used to update data for checker_class from answers.py
  
  then, if length of guesses is more than 5 and the game is not in the last chance to answer, it gets good tries to find out more letters.
  
  after this, a random button is pressed to see if the game has ended or shown a result and if it has, it resets all data
  
