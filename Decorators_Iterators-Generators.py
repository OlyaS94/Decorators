#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json


class get_links:

    def __init__(self, source):
        with open(str(source)) as file:
            self.countries = json.load(file)
        self.start = -1
        self.end = len(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        name = self.countries[self.start]['name']['common']
        return f'Country name: {name}, '                f'Wiki Link: https://en.wikipedia.org/wiki/{name.replace(" ", "_").replace(",", "_")} \n'
import time

def logger(my_file):
    def decorator(function):
        def wrapper(*args, **kwargs):
            with open(my_file, 'a') as file:
                result = function(*args, **kwargs)
                file.write(f'Время вызова - {time.asctime()} \n'
                           f'Имя функции - {function.__name__} \n'
                           f'Аргументы - {args}, {kwargs} \n'
                           f'Результат - {result} \n\n')
                return result
        return wrapper
    return decorator

@logger('logger.txt')
def hash_generator(filename):
    file = open(str(filename))
    for line in file.readline():
        yield hash(line)
    file.close()


if __name__ == '__main__':
    with open('countries_wiki.txt', 'w', encoding='utf-8') as f:
        for country in get_links('countries.json'):
            f.write(country)

    for a in hash_generator('countries_wiki.txt'):
        print(a)


# In[1]:





# In[ ]:




