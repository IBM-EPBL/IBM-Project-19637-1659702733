from locust import HttpUser, task

class WebsiteUser(HttpUser): 
    
    @task 
    def index(self): 
        self.client.get(url='/')
    @task 
    def task1(self): 
        self.client.get(url='/login') 
    
    @task 
    def task2(self): 
        self.client.get(url='/openaddcategory')

    @task 
    def task3(self): 
        self.client.get(url='/addcat')

    @task 
    def task4(self): 
        self.client.get(url='/opendelcategory')

    @task 
    def task5(self): 
        self.client.get(url='/delcat')

    @task 
    def task6(self): 
        self.client.get(url='/openupcategory')

    @task 
    def task7(self): 
        self.client.get(url='/upcat')

    @task 
    def task8(self): 
        self.client.get(url='/openviewcategory')


    @task 
    def task9(self): 
        self.client.get(url='/openviewcat')

   

