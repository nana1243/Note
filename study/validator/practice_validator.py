from pydantic import BaseModel, validator


class UserModel(BaseModel):
    """
    어떤 값을 검증을 하려고 할때 `Validator` 를 기억하자!
    참고문서:
        https://pydantic-docs.helpmanual.io/usage/validators/
    """

    name: str
    username: str
    password1: str
    password2: str

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("must contain a space")
        return v.title()

    @validator("password2")
    def passwords_match(cls, v, values, **kwargs):
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v

    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), "must be alphanumeric"
        return v


user = UserModel(
    name="samuel colvin",
    username="scolvin",
    password1="zxcvbn",
    password2="zxcvbn",
)
print(user)