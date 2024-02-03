# Định nghĩa Subject (Chủ thể)
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

# Định nghĩa Observer (Quan sát viên)
class Observer:
    def update(self, message):
        pass

# Triển khai Subject cụ thể
class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._news = None

    def set_news(self, news):
        self._news = news
        self.notify_observers(news)

# Triển khai Observer cụ thể
class NewsReader(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} đọc tin tức mới: {message}")

# Sử dụng
if __name__ == "__main__":
    # Tạo chủ thể (subject)
    news_agency = NewsAgency()

    # Tạo các quan sát viên (observers)
    reader1 = NewsReader("Độc giả 1")
    reader2 = NewsReader("Độc giả 2")

    # Đăng ký quan sát viên cho chủ thể
    news_agency.add_observer(reader1)
    news_agency.add_observer(reader2)

    # Đặt tin tức mới, tất cả các quan sát viên sẽ được thông báo và cập nhật
    news_agency.set_news("Có một sự kiện quan trọng diễn ra!")

    # Kết quả:
    # Độc giả 1 đọc tin tức mới: Có một sự kiện quan trọng diễn ra!
    # Độc giả 2 đọc tin tức mới: Có một sự kiện quan trọng diễn ra!
