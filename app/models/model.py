from pydantic import BaseModel,EmailStr,validator

# Pydantic schema for the Users [It is used in register.py]
class UserDetail(BaseModel):
    UserName: str
    Email: EmailStr
    Password: str
    Role: str
    Id: int

    @validator('Password')
    def validate_password(cls,u):
        if len(str(u)) < 8:
            raise ValueError('Password should contain minimum 8 Characters.......')
        return u

# Pydantic schema for the Shipments [It is used in new_shipment.py]
class ShipmentDetails(BaseModel):
    Id:int
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

    @validator('ShipmentNumber')
    def validate_ShipmentNumber(cls,v):
        if len(str(v)) != 7:
            raise ValueError('Shipment Number must contain 7 digits......')
        return v


# Pydantic schema for the feedback [It is used in feedback.py]    
class FeedbackDetails(BaseModel):
    name: str
    Email: str
    rating: int
    opinion: str