import os
import pandas 
import csv 

class User:
    def __init__(self):
        if 'user.csv' not in os.listdir('./'):
            with open('user.csv', 'w') as f:
                csv.writer(f).writerow(['id', 'problems'])
        
        self.df = pandas.read_csv('./user.csv')

    def check_user_exist(self, id):
        if id not in list(self.df['id']):
            return 0
        
        else:
            return 1

    def add_user(self, id, problems = ''):
        if self.check_user_exist(id) == 1:
            return 'UserDuplicateError'

        self.df.loc[len(self.df)] = [id, problems]

    def find_user_row(self, id):
        if self.check_user_exist(id) == 0:
            return 'UserNotExistError'
        
        else:
            for n, i in enumerate(self.df['id']):
                if i == id:
                    return n
        
    def add_user_resolved_problems(self, id, problems):
        if self.check_user_exist(id) == 0:
            return 'UserNotExistError'
        
        else:
            index = self.find_user_row(id)
            self.df.iloc[index, 1] = self.make_resolved_problem_string(problems)

    def make_resolved_problem_string(self, problems):
        string = ''

        for i in problems[:len(problems) - 1]:
            string += f'{i} '
        
        return string + problems[len(problems) - 1]

    def user_resolved_problems(self, id):
        if self.check_user_exist(id) == 0:
            return 'UserNotExistError'
        
        else:
            index = self.find_user_row(id)
            return self.df.iloc[index, 1] 

    def save_csv(self):
        self.df.to_csv('user.csv', index=False, header = True)

        