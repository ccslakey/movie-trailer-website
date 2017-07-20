import media

m1_poster = "http://www.gstatic.com/tv/thumb/dvdboxart/175320/p175320_d_v8_ac.jpg"
m2_poster = "http://www.gstatic.com/tv/thumb/movieposters/5588/p5588_p_v8_au.jpg"
m3_poster = "https://s-media-cache-ak0.pinimg.com/originals/81/76/18/8176180953311ef1d6efa99af8254dcd.jpg"

m1 = media.Movie("Forgetting Sarah Marshall",
                             m1_poster,
                             "https://www.youtube.com/watch?v=PyVEHIO6jZ0")

m2 = media.Movie("Seven Samurai",
                            m2_poster,
                            "https://www.youtube.com/watch?v=bBfgNpSQm3I")

m3 = media.Movie("Star Wars Episode V - The Empire Strikes Back",
                          m3_poster,
                          "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

movies = [m1, m2, m3]
