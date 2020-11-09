from django import forms
from .models import Product


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('title 은 3글자 이상 입력해 주세요!')


class registerForm(forms.Form):
    category_list = ['자전거', '식기류', '전자기기', '가구', '기타']
    CATEGORY_CHOICE = tuple(enumerate(category_list))

    # author = models.ForeignKey(MyUser, on_delete=models.CASCADE) #작성자

    # 제목 최소 세글자 이상
    name = forms.CharField(label= "제목", validators=[min_length_3_validator])

    # 이미지 업로드
    photo = forms.ImageField(label= "이미지")

    # 글 내용
    content = forms.CharField(label= "내용", widget=forms.Textarea)

    # 최소 가격
    min_price = forms.IntegerField(label= "시작 가격", )

    # 카테고리 선택
    category = forms.ChoiceField(label= "분류", choices=CATEGORY_CHOICE)

    def save(self, commit=True):
        post = Product(**self.cleaned_data)
        if commit:
            post.save()
        else:
            return post



