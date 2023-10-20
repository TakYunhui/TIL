from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )

    # override
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # 읽기 전용 필드 - 유효성 검사에서 제외
        # => article override로 주석 처리
        # read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 나를 참조하는 모든 댓글 정보 다 가져오겠다
        # serializer 의 목적: 가지고 온 데이터를 사용자에게 어떻게 보여줄 지 정의
    comment_set = CommentSerializer(many=True, read_only=True)
    # 내가 마음대로 정의한 변수명. 다른 이름으로 해도 상관 없음
    # comment_set과 같이 역참조 매니저명은 django가 기존에 정의해놓은 것

    # 'comment_count' 해당 변수는 내가 새롭게 정의한 것, 변수에 할당될 값도 내가 정의
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


        
