# Suppose we are bettin $100 on a fair coin flips
# If n consecutive coin flips results in all heads we win else we lose
# We can bet as many times as we want
# Suppose we bet x times,
# Find the probability that we win the bet at least once?
# What is the expected payout to break even?

def coin_flips(n, x):
  
  bet = 100
  probability_of_win = 0.5
  
  chance_of_winning_a_single_trial = probability_of_win**n
  chance_of_losing_a_single_trial = 1 - chance_of_winning_a_single_trial
  
  chance_of_losing_x_trials_in_a_row = chance_of_losing_a_single_trial**x
  chance_of_winning_x_trials_in_a_row = 1 - chance_of_losing_x_trials_in_a_row
  
  expected_payout = bet/float(chance_of_winning_x_trials_in_a_row)
  
  return [chance_of_winning_x_trials_in_a_row*100, expected_payout]

n = 10
x = 5

coin_flips(n,x)
