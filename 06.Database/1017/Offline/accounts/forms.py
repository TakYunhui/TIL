from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# 유저 생성을 위한 form이 있지만 바꿔써야 하는 이유
# 기본 제공 UserCreationForm은 model로 auth.User을 쓰고 있으나
# 우리는 accounts.User 쓸 거다 
class CustomUserCreationForm(UserCreationForm):
    # Meta class 상속받아 쓰는 이유
    # 우리는 Meta class에서 model, field, exclude 정도를 쓴다
    class Meta(UserCreationForm.Meta):
        model = User
        