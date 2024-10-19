class alamo_class:
    def __init__(self, class_type: str,
                 model: str,
                 pax: str,
                 lug: str,
                 data_dtm_track: str,
                 date_scr_date: str,
                 date_scr_int: int,
                 date_rsv_date: str,
                 date_rsv_int: int,
                 adv_rsv: int,
                 cost_daily: str,
                 cost_total: str,
                 ) -> None:
        self.service = "Alamo"
        self.class_type = class_type # SUV, sedan, minivan, etc
        self.model = model # Vehicle description
        self.pax = pax # passenger capacity
        self.lug = lug # luggage space
        self.date_scr_date = date_scr_date
        self.date_scr_int = date_scr_int
        self.date_rsv_date = date_rsv_date
        self.date_rsv_int = date_rsv_int
        self.adv_rsv = adv_rsv
        self.data_dtm_track = data_dtm_track # css attribute
        self.cost_daily = float(cost_daily)
        self.cost_total = float(cost_total)


if __name__ == "__main__":

    my_car = alamo_class("Full Size", "Nissan Altima or similar", "car_class|pay_later|CFAR", "125.01", "150.20")

    print(my_car.__dict__)