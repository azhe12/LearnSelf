# coding=utf-8
import webbrowser
class Movie():
    '''a movie class
    
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''构造函数
        
        :param movie_title: string 标题 
        :param movie_storyline: string 故事情节
        :param poster_image: string 宣传图链接
        :param trailer_youtube: string 预告片链接
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''显示预告
        
        :return: 
        '''
        webbrowser.open(self.trailer_youtube_url)

# print(Movie.__doc__)
help(Movie)