##### pydantic
from pydantic import BaseModel

class newsPostModel(BaseModel):
	pass

class RACModel(BaseModel):
	user_id:int
	position:int
	rate:int
	comment:str
	comment_number:int