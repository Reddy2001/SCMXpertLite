from pydantic import BaseModel,EmailStr,validator

# Pydantic schema for the Users [It is used in register.py]
class UserDetail(BaseModel):
    UserName: str
    Email: EmailStr
    Password: str
    Role: str


# Pydantic schema for the Shipments [It is used in new_shipment.py]
class ShipmentDetails(BaseModel):
    Email:str
    ShipmentNumber: int
    ContainerNumber: int
    RouteDetails: str
    GoodsType: str
    DeviceName: str
    DeliveryDate: str
    PO_Number: int
    DeliveryNumber: int
    NDC_Number: int
    BatchId: int
    SerialNumber: int
    ShipmentDescription: str


# Pydantic schema for the feedback [It is used in feedback.py]    
class FeedbackDetails(BaseModel):
    name: str
    Email: str
    rating: int
    opinion: str