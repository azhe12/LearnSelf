# coding=utf-8
import webbrowser
class Movie():
    # 构造函数
    # @movie_title string 标题
    # @movie_storyline string 故事情节
    # @poster_image string 宣传图链接
    # @trailer_youtube string 预告片链接
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # 显示预告片
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)