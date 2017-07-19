# coding=utf-8
import media
import fresh_tomatoes


# 火影忍者
Naruto = media.Movie("NARUTO",
                        'A ninja world.',
                        'http://www.91uu.com/uploads/allimg/140605/24-1406051P414610.jpg',
                        'https://www.youtube.com/watch?v=9s-ddbg8sts')

# 千与千寻
Qianxun = media.Movie("QIANXUN",
                      "A Japanese girl have a fantastic travel",
                      "https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=10eab8e7e41190ef15f69a8daf72f673/4afbfbedab64034fed2faa0cacc379310b551ddd.jpg",
                      "https://www.youtube.com/watch?v=hLTOdC_1mXg")


# 让子弹飞
Zidanfei = media.Movie("Let the Bullets Fly",
                           "chinese style story",
                           "https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=456b67b0ebc4b7452099bf44ae957572/1c950a7b02087bf445efb670f2d3572c11dfcf2c.jpg",
                           "https://www.youtube.com/watch?v=33SjTgWt1gI")

movies = [Naruto, Qianxun, Zidanfei]
fresh_tomatoes.open_movies_page(movies)

