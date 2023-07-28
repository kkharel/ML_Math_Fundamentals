# Suppose we carried out a test indicating the presence of mental condition of being toxic at workplace
# The test is 95% accurate in both sensitivity and specificity
# We also found that only 3% of co-workers have mental condition of being toxic i.e prevelance of mental condition
# If a co-worker tests positive(negative) for mental condition,
# What is the probability that your co-worker is toxic (is not) toxic?

# The probability that your co-worker has mental condition of toxicity given positive test result
# The probability that your co-worker does not have a mental condition given negative test result

# Assume sensitivity and specificity = accuracy

def probability_of_toxicity(accuracy, prevalence):
    testing_positive_given_toxicity_present = accuracy
    testing_negative_given_toxicity_not_present = accuracy

    percent_of_toxic_users = prevalence
    percent_of_non_toxic_users = 1 - prevalence

    testing_positive_given_toxicity_not_present = 1 - accuracy
    testing_negative_given_toxicity_present = 1 - accuracy

    positive = (percent_of_toxic_users * testing_positive_given_toxicity_present) + (percent_of_non_toxic_users * testing_negative_given_toxicity_present)
    negative = 1 - positive

    user_has_toxicity_given_positive_test_result = (percent_of_toxic_users * testing_positive_given_toxicity_present) / positive
    user_does_not_have_toxicity_given_negative_test_result = (percent_of_non_toxic_users * testing_negative_given_toxicity_not_present) / negative

    return [user_has_toxicity_given_positive_test_result * 100, user_does_not_have_toxicity_given_negative_test_result * 100]

accuracy = 0.95
prevalence = 0.03

probability_of_toxicity(accuracy, prevalence)

