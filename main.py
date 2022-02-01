import random
import math

def main():

    #answer values in dictionary, question and gender values in lists
    answers = {'gate': ['porta', 'portae', 'portae', 'portam', 'porta'],
               'gates': ['portae', 'portarum', 'portis', 'portas', 'portis'],
               'friend': ['amicus', 'amici', 'amico', 'amicum', 'amico'],
               'friends': ['amici', 'amicorum', 'amicis', 'amicos', 'amicis']
               }
    words = list(answers.keys())
    genders = ['f', 'f', 'm', 'm']

    # question and answer randomizer
    # question and answer copies allow for pop() to not destroy the original data
    answers_temp = answers.copy()
    words_temp = words.copy()
    genders_temp = genders.copy()
    # the random lists will contain scrambled data
    answers_rand = {}
    words_rand = []
    genders_rand = []
    c: int = 0
    for b in range(len(words) - 1, -1, -1):
        # generate a random number based on the shrinking list lengths
        rand_index = math.floor(random.random() * (b + 1))
        words_rand.append(words_temp.pop(rand_index))
        answers_rand[words_rand[c]] = answers_temp[words_rand[c]]
        genders_rand.append(genders_temp.pop(rand_index))
        c += 1

    # sentinel value and control variable
    mainLoopContinue = True

    while mainLoopContinue:
        # track number of correct answers
        num_total = 0
        num_correct = 0

        for a in range(len(words_rand)):

            # create a question:
            question = words_rand[a][0].upper() + words_rand[a][1:] + f' ({genders_rand[a]})' + ': '
            # get user string
            print('')
            input_whole = input(question)

            # input as individual lines (held in a list)
            input_words = input_whole.split(' ')

            # iterate through and return valid and invalid answers
            answer_validation = ''
            for i in range(5):
                if i < len(input_words):
                    if input_words[i] == answers_rand[words_rand[a]][i]:
                        answer_validation += input_words[i] + ' (CORRECT) '
                        num_correct += 1
                        num_total += 1
                    else:
                        answer_validation += input_words[i] + f' (WRONG: {answers_rand[words_rand[a]][i]}) '
                        num_total += 1
                else:
                    answer_validation += f'(WRONG: {answers_rand[words_rand[a]][i]}) '
                    num_total += 1

            # show user correct and incorrect answers
            print(answer_validation)

        # show performance results
        ratio = math.floor(((num_correct / num_total) * 100))
        print(f'\nPERFORMANCE: {num_correct} out of {num_total} ({ratio}%)')

        userChoice = input('Would you like to try again for a higher score? [Y/n]: ')
        if userChoice.lower() == 'n' or userChoice.lower() == 'no':
            mainLoopContinue = False


if __name__ == '__main__':
    main()