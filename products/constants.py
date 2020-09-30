from tech_shop.enum import DjangoEnum


DISCOUNT = 0.20  # 20% discount


class StatusChoices(DjangoEnum):
    COMPLETED = "Completed"
    PAID = "Paid"
    NEW = "New"
    IN_PROGRESS = "In progress"
