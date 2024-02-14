
from pydantic import BaseModel

# Pydantic schema for the Users
class UserDetail(BaseModel):
    name: str
    mail: str
    password: str
    con_password: str


# Pydantic schema for the Shipments
class Shipment(BaseModel):
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
    
