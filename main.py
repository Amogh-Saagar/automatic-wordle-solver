import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from answer import checker_class

grey = []
correct = [None, None, None, None, None]
yellow = []
yellow_all = []
yellow_hist = []
word_hist = []
en = open("en5-new", 'r').read().split()
eng = open('eng-new', 'r').read().split()
guesses = en
gusses_cache = []
goodtry = []
x = 0
green = []
alpha = []
run = True
text = 'guest'
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.wordleunlimited.com/')
time.sleep(1)
n_letter = driver.find_elements(By.XPATH, f"//div[contains(text(),'n')]")[-1]
alphab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
for i in alphab:
    alpha.append(driver.find_element(By.XPATH, f"//div[contains(text(),'{i}')]"))
    time.sleep(0.08)
alpha[13] = n_letter
keys = {'RowL-letter letter-absent': 'grey', 'RowL-letter letter-correct': 'green',
        'RowL-letter letter-elsewhere': 'yellow'}


def enter_text(t):
    time.sleep(0.05)
    for i in t:
        alpha[alphab.index(i)].click()
    submit = driver.find_element(By.XPATH, f"//div[contains(text(),'Enter')]")
    submit.click()


def get_good(en, used, x=0):
    rank = 0
    if rank > 3:
        return None
    goodtry = []
    for i in en:
        for j in used:
            rank += i.count(j)
        if rank <= x:
            goodtry.append(i)
        rank = 0
    if len(goodtry) == 0:
        x += 1
        get_good(en, used, x)
    return goodtry


all_grey = []

no = 0

while no != 6:
    if no == 0:
        print('ran')
        enter_text('guest')
        text = 'guest'
    field1 = driver.find_elements(By.XPATH, "//div[@class = 'RowL RowL-locked-in']")
    run = True
    while run:
        if not len(field1) == no + 1:
            if len(guesses) < 3:
                for word in en:
                     checker = checker_class(word, correct, yellow_all, yellow_hist, word_hist, all_grey)
                     if checker.run():
                        gusses_cache.append(word)
                guesses = gusses_cache
            text = random.choice(guesses)
            for las in range(5):
                driver.find_element(By.XPATH, '//*[text()= "⌫"]').click()
            enter_text(text)
            field1 = driver.find_elements(By.XPATH, "//div[@class = 'RowL RowL-locked-in']")
        else:
            run = False
    try:
        driver.find_element(By.XPATH, '//div[@class= "btn btn-success"]').click()
    except:
        pass
    field = field1[-1]

    field = field.find_elements(By.TAG_NAME, 'div')
    for n, i in enumerate(field):
        name = keys[i.get_attribute('class')]
        if name == 'yellow':
            yellow.append(i.get_attribute('textContent'))
        elif name == 'grey':
            grey.append(i.get_attribute('textContent'))
        elif name == 'green':
            green.append(i.get_attribute('textContent'))
            correct[n] = i.get_attribute('textContent')


    yellow_all += yellow
    yellow_all = list(set(yellow_all))
    yellow_hist.append(yellow)
    word_hist.append(text)
    used = list(set(yellow + grey + green))
    all_grey += grey
    all_grey = list(set(all_grey))
    all_grey_cache = []
    A = [i for i in all_grey if i not in correct and i not in yellow_all]

    all_grey = all_grey_cache
    list1 = guesses
    try:
        enter_text('a')
        driver.find_element(By.XPATH, '//*[text()= "⌫"]').click()
    except:
        pass

        no = 0
    # if no > 3:
    #     gusses_cache = get_good(eng, used)
    #     guesses = gusses_cache
    # else:
    guesses = []
    guesses_cache = []
    for word in en:
        checker = checker_class(word, correct, yellow_all, yellow_hist, word_hist, all_grey)
        if checker.run():
            gusses_cache.append(word)
    guesses = gusses_cache
    gusses_cache = []
    if len(guesses) > 5 or no < 5:

        gusses_cache = get_good(eng, used)
        if len(gusses_cache) != 0 and gusses_cache is not None:
            print('null')
            guesses = gusses_cache	
    text = random.choice(guesses)
    if text in word_hist:
        text = random.choice(guesses)
    yellow = []
    no += 1
    if len(driver.find_elements(By.XPATH, "//div[@class = 'RowL RowL-locked-in']")) == 0:
        yellow = []
        grey = []
        correct = [None, None, None, None, None]
        green = []
        text = 'guest'
        all_grey = []
        yellow_all = []
        yellow_hist = []
        no = 0	
        word_hist = []

