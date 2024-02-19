from pydantic import BaseModel,EmailStr

# Pydantic schema for the Users
class UserDetail(BaseModel):
    UserName: str
    Email: EmailStr
    Password: str
    Role: str


# Pydantic schema for the Shipments
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


# Pydantic schema for the feedback    
class feedbackDetails(BaseModel):
    name: str
    Email: str
    rating: int
    opinion: str