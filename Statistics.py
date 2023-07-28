def get_statistics(input_list):
    # Write your code here.
    return {
        "mean": mean(input_list),
        "median": median(input_list),
        "mode": mode(input_list),
        "sample_variance": sample_variance(input_list),
        "sample_standard_deviation": sample_standard_deviation(input_list),
        "mean_confidence_interval": mean_confidence_interval(input_list),
    }

def mean(arr):
    if len(arr) == 0:
        return 0
    return sum(arr)/len(arr)

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        value = (arr[n//2-1]+arr[n//2])/2
    else:
        value = arr[n//2]
    return value

def mode(arr):
    dict = {}
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    max_val = float("-inf")
    max_val_key = None
    for i,j in dict.items():
        if j > max_val:
            max_val = j
            max_val_key = i
    return max_val_key


def sample_variance(arr):
    n = len(arr)
    mean = sum(arr)/n # check here later
    sq_diff = []
    for i in arr:
        difference = i - mean
        sq_diff.append(difference**2)
    if n < 2:
        raise ValueError("Sample size must be at least 2")
    variance = sum(sq_diff)/(n-1)
    return variance

def sample_standard_deviation(arr):
    stdev = (sample_variance(arr))**(1/2)
    return stdev

def mean_confidence_interval(arr):
    mean_se = sample_standard_deviation(arr) / (len(arr)**0.5)
    z_score_se = 1.96*mean_se
    mean_ci = [mean(arr) - z_score_se, mean(arr) + z_score_se]
    return mean_ci
