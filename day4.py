input = './input/day_4'

with open(input, 'r') as f:
    file = f.readlines()

total_count = 0
cards = {}
i = 1

for line in file:
    matches = 0
    card_split = line.strip().split(':')

    game_split = card_split[1].strip().split('|')
    winners = set(game_split[0].split(' '))

    my_nums = game_split[1].split(' ')
    for number in my_nums:
        if number:
            if number in winners:
                matches += 1
    cards[i] = matches
    i += 1

def evaluate_games(card_id):
    globals()['total_count'] += 1

    if cards[card_id] == 0:
        return 0

    matches = cards[card_id]

    for card in range(card_id+1, card_id+matches+1):
        evaluate_games(card)

for card in range(1, i):
    evaluate_games(card)

print(total_count)
