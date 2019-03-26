import user
import crawller

userObj = user.User()
crawllerObj = crawller.Crawller()

problems = open('problems.txt', 'r').readline().split()
members = open('members.txt', 'r').readline().split()

for i in members:
    print(crawllerObj.get_info_from_id(i))
