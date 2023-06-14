def fetch_coursera_course(course_code):
        coursera = CourseraScrapper()
        course = coursera.scrap_course(course_code)

    def fetch_coursera_course_details(course_code):
        coursera = CourseraScrapper()
        course = coursera.scrap_course_details(course_code)
    
    def fetch_coursera_course_schedule(course_code):
        coursera = CourseraScrapper()
        course = coursera.scrap_course_schedule(course_code)
    
    def fetch_coursera_course_prerequisites(course_code):
        coursera = CourseraScrapper()
        course = coursera.scrap_course_prerequisites(course_code)
    
    def fetch_coursera_course_instructors(course_code):
        coursera = CourseraScrapper()
        course = coursera.scrap_course_instructors(course_code)
    
    def fetch_coursera_course_reviews(course_code):
        coursera = CourseraScrapper()
        course = coursera.scrap_course_reviews(course_code)



        ---

        def fetch_sia_course(course_code):
        sia = SiaScrapper()
        course = sia.scrap_course(course_code)
    
    def fetch_sia_course_details(course_code):
        sia = SiaScrapper()
        course = sia.scrap_course_details(course_code)
    
    def fetch_sia_course_schedule(course_code):
        sia = SiaScrapper()
        course = sia.scrap_course_schedule(course_code)
    
    def fetch_sia_course_prerequisites(course_code):
        sia = SiaScrapper()
        course = sia.scrap_course_prerequisites(course_code)
    
    def fetch_sia_course_instructors(course_code):
        sia = SiaScrapper()
        course = sia.scrap_course_instructors(course_code)