class alamo_class:
    def __init__(self, class_type: str, model: str,
                 pax: str, lug: str,
                 data_dtm_track: str, cost_daily: str,
                 cost_total:str) -> None:
        self.class_type = class_type # SUV, sedan, minivan, etc
        self.model = model # Vehicle description
        self.pax = pax # passenger capacity
        self.lug = lug # luggage space
        self.data_dtm_track = data_dtm_track # css attribute
        self.cost_daily = f"${cost_daily}"
        self.cost_total = f"${cost_total}"


if __name__ == "__main__":

    my_car = alamo_class("Full Size", "Nissan Altima or similar", "car_class|pay_later|CFAR", "125.01", "150.20")

    print(my_car.__dict__)