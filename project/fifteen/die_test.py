from die import Die 
import pytest

# 扔骰子，若扔的次数不合理，错误提醒，程序异常，若合理，则将出现的数字放入results数组中
def roll_die(num_rolls):
    if num_rolls <= 0:
        raise ValueError("Number of rolls must be a positive integer.")
    
    die = Die()
    results = []
    
    for roll_num in range(num_rolls):
        result = die.roll()
        results.append(result)
        
    return results

# 统计骰子每个面出现的次数并保存到数组中
def analyze_results(results, num_sides):
    frequencies = []
    poss_results = range(1, num_sides + 1)
    
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)
    
    return frequencies

# 测试代码
# 测试代码
def test_roll_die():
    # 测试参数错误的情况
    with pytest.raises(ValueError):
        roll_die(-1)
    
    # 测试实际结果是否正确
    results = roll_die(1000)
    
    #results = roll_die(-1000)
    
    assert len(results) == 1000
    assert min(results) >= 1
    assert max(results) <= 6
    
    frequencies = analyze_results(results, 6)
    assert sum(frequencies) == 1000
    
    print("每个面出现的次数：")
    for i in range(6):
        print("面{}出现了{}次".format(i+1, frequencies[i]))


# 执行测试
test_roll_die()
