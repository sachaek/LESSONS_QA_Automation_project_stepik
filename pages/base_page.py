from typing import Union

from selenium import webdriver


class BasePage():
    def __init__(self, browser: Union[webdriver.Chrome, webdriver.Firefox], url):
        self.browser = browser
        self.url = url
        """Теперь в наш класс нужно добавить методы. Первым 
        делом добавим конструктор — метод, который вызывается, 
        когда мы создаем объект. Конструктор объявляется ключевым 
        словом __init__. В него в качестве параметров мы передаем 
        экземпляр драйвера и url адрес. Внутри конструктора сохраняем 
        эти данные как аттрибуты нашего класса"""

    def open(self):
        self.browser.get(self.url)
        """Теперь добавим еще один метод open. Он должен 
        открывать нужную страницу в браузере, используя метод get()."""
