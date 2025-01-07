from math import sqrt
def divide(quo, div):
    return{b:[c for c in div if c%b == 0]for b in quo }

def display(fruit, count):
    """Display a count of a fruit in square brackets.

    >>> display('apples', 3)
    '[3 apples]'
    >>> display('apples', 1)
    '[1 apple]'
    >>> print(display('apples', 3) + display('kiwis', 3))
    [3 apples][3 kiwis]
    """
    assert count >= 1 and fruit[-1] == 's'
    if count == 1:
        fruit = fruit[:-1]  # get rid of the plural s
    return '[' + str(count) + ' ' + fruit + ']'

def buy(fruits_to_buy, prices, total_amount):
    def helper(amount, money, index):
        if money == 0: 
            for i in range(len(fruits_to_buy)):  print(display(fruits_to_buy[i], amount[i]))
        elif index == len(fruits_to_buy): return
        else:
            for i in range(money//prices[fruits_to_buy[index]]+1):
                amount[index] += i
                helper(amount, money - prices[fruits_to_buy[index]]*i, index+1)
                amount[index] -= i
    amount = []
    money = 0
    for i in range(len(fruits_to_buy)): 
        money += prices[fruits_to_buy[i]]
        amount.append(1)
    return helper(amount, total_amount - money, 0)

def make_city(name, lat, lon):
    return [name, lat, lon]
def get_name(city):
    return city[0]
def get_lat(city):
    return city[1]
def get_lon(city):
    return city[2]

def distance(city_a, city_b):
    print(sqrt((get_lat(city_a)-get_lat(city_b))**2 + (get_lon(city_a)-get_lon(city_b))**2)) 

# city_a = make_city('city_a', 0, 1)
# city_b = make_city('city_b', 0, 2)
# distance(city_a, city_b)
# city_c = make_city('city_c', 6.5, 12)
# city_d = make_city('city_d', 2.5, 15)
# distance(city_c, city_d)

def closer_city(lat, lon, city_a, city_b):
    dis_a = sqrt((get_lat(city_a)-lat)**2 + (get_lon(city_a)-lon)**2)
    dis_b = sqrt((get_lat(city_b)-lat)**2 + (get_lon(city_b)-lon)**2)
    if dis_a < dis_b : print(get_name(city_a))
    else : print(get_name(city_b))

berkeley = make_city('Berkeley', 37.87, 112.26)
stanford = make_city('Stanford', 34.05, 118.25)
closer_city(38.33, 121.44, berkeley, stanford)
bucharest = make_city('Bucharest', 44.43, 26.10)
vienna = make_city('Vienna', 48.20, 16.37)
closer_city(41.29, 174.78, bucharest, vienna)