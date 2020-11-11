from django import forms
from .models import Product


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('title 은 3글자 이상 입력해 주세요!')


class registerForm(forms.Form):
    category_list = ['디지털/가전', '가구/인테리어', '생활용품', '의류', '게임/취미', '도서/티켓/음반']
    CATEGORY_CHOICE = tuple(enumerate(category_list))

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



