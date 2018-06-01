import unittest



class Locator(object) :

    # school list

    next_button = "//button[@class= 'next land-page-btn']"                    
    school_list = '/html/body/div[3]/div/div/div[1]/div[2]/ul/li'
   

    # role

    student = "/html/body/div[3]/div/div/div[2]/div[1]"

    # login

    username = "//input[@name='username']"
    password = "//input[@name ='password']"
    login = "login-sub"

    # landing page
    confirmation_modal = '.intro-welcome-overlay'
    yes_button = ".btn.btn-success.btn-large.large-font"

    learn = "/html/body/div[3]/div/div/div[2]/div[1]/div[1]/a"
    quiz = "/html/body/div[3]/div/div/div[2]/div[1]/div[2]/a"
    logout = "/html/body/div[3]/div/div/div[1]/div/div/a/span"
    pop_up = "/html/body/div[3]/div[2]/div[1]/div[1]/div/p/span"

    # welcome pop up

    welcome_pop_up = "//div[contains(@class , 'welcome-screen-zaya')]"
    welcome_next_button = ".btn.btn-info.btn-block"

    # learn 

    right_header_score = "/html/body/div[3]/div[1]/div[1]/div[3]/span"
    course_list = "/html/body/div[3]/div[2]/div[2]/div/ul/li"
    lesson = "lesson-3"
    lesson_list = ".lessons-list.list-unstyled > div > li"
    start_lesson = ".lessons-list.list-unstyled > div > li > button > strong"
    
    # student resources page

    lesson_intro_pop_up = "//div[contains(@class , 'intro-welcome-overlay')]"
    take_ride_button = ".btn.btn-success.btn-large.medium-font"
    skip = "//div[contains(@class , 'introjs-skipbutton')]"

    resources_list = "//*[@id='student_resourse']/div"
  

    video = "//div[contains(@class , 'video')]"
    video_deactive = "//div[contains(@class , 'video-deactive')]"
    node_active = ".node.transition-bounce.ng-scope.node-active.pdf-active"
    node_deactive = ".node.transition-bounce.ng-scope.node-deactive.pdf-deactive"
    practice = "//div[contains(@class , 'practice')]"
    practice_deactive = "//div[contains(@class , 'practice-deactive')]"
    quiz_active = ".node.transition-bounce.ng-scope.quiz-active.node-active"
    quiz_deactive = ".node.transition-bounce.ng-scope.quiz-deactive.node-deactive"

    # practice

    practice_level_list = "//ul[contains(@class ,'level-list')]/li"

    highest_score = ".hi-score.ng-hide"
    recent_score = ".level-points.small-font.ng-binding.color-easy"

    start_button = ".level-cta-btn.ng-binding.btn-easy.btn-easy-img.level-btn-txt"

    # practice_question_type

    submit = '.qstn-sub.bbtn.pull-left'
    go_prev_question = ".qstn-pager.qstn-prev"
    go_next_question = ".qstn-pager.qstn-nxt"
    intro = ".intro-welcome-overlay.ng-scope"


    SCQ = ".row.qstn-block.type-SCQ"
    SCQ_options_list = ".list-unstyled.ans-list.ng-scope > li"
    SCQ_option = ".list-unstyled.ans-list.ng-scope > li:nth-child({})"
    
    MCQ = ".row.qstn-block.type-MCQ"

    DR = ".row.qstn-block.type-DR"
    input_field = "practiceAnswers"

    SST = ".row.qstn-block.type-SST"
    SOR = ".row.qstn-block.type-SOR"

    PUZ = ".row.qstn-block.type-PUZ"
    stick_list = "stick.pic.stick-bck-fill.ng-scope.ui-sortable-handle"
    container = ".drop-container.transition-color.ng-pristine.ng-valid.ui-sortable.pic-drop-container-fill"

    MTF = ".row.qstn-block.type-MTF"




    # http://home.zaya.in/learn/?alias=demo-school#/class/224/course/305/lesson/8557/practice/70285a3d-1872-4851-b93e-32f71d1b1f88


