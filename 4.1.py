# Homework-session-4
def display_movie(m):
    print("Original name: ", m["org_name"])
    print("translated name: ", m["trans_name"])
    print("year: ", m["year"])
    print()

def create_movie(org_name, trans_name, year):
    return {
        "org_name":org_name,
        "trans_name": trans_name,
        "year": year
    }
##
##movie0 = create_movie("The hunger games", "Đấu trường sinh tử", 2016)
##display_movie(movie0)

def display_movie_list(m_list):
    j = 0
    for i in m_list:
       j +=1
       print("Movie#{0}".format(j))
       for key,value in i.items(): 
           print("{0}: {1}".format(key,value))
       print()   

##movie_list=[]
##movie0 = create_movie("The hunger games", "Đấu trường sinh tử", 2016)
##movie1 = create_movie("Little Door Gods", "Tiểu Môn Thần", 2015)
##movie_list.append(movie0)
##movie_list.append(movie1)
##display_movie_list(movie_list)

def remove_movie(m_list, movie):
    if movie == movie0 :  m_list.pop(0)
    else: m_list.pop(1)

##movie0 = create_movie("The hunger games", "Đấu trường sinh tử", 2016)
##movie1 = create_movie("Little Door Gods", "Tiểu Môn Thần", 2015)
##movie_list = [movie0, movie1]
##remove_movie(movie_list, movie0)
##display_movie_list(movie_list)


def search_movie_by_year(m_list, year):
    search_list =[]
    for i in m_list:
        if i["year"] == year:
            search_list.append(i)
    return(search_list)
            
movie_list=[]
movie_list.append(create_movie("The hunger games", "Đấu trường sinh tử", 2016))
movie_list.append(create_movie("Break point", "Ranh giới chết", 2015))
movie_list.append(create_movie("Little Door Gods", "Tiểu Môn Thần", 2015))
movie_in_2015 = search_movie_by_year(movie_list, 2015)
display_movie_list(movie_in_2015)
