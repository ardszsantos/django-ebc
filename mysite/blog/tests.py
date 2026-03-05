import pytest
from django.contrib.auth.models import User
from blog.models import Post


@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def post(db, user):
    return Post.objects.create(
        title='Test Post',
        slug='test-post',
        author=user,
        content='Test content',
        status=1,
    )


@pytest.mark.django_db
def test_post_creation(post):
    assert post.title == 'Test Post'
    assert post.slug == 'test-post'
    assert post.status == 1


@pytest.mark.django_db
def test_post_str(post):
    assert str(post) == 'Test Post'


@pytest.mark.django_db
def test_post_default_status(db, user):
    post = Post.objects.create(
        title='Draft Post',
        slug='draft-post',
        author=user,
        content='Draft content',
    )
    assert post.status == 0


@pytest.mark.django_db
def test_post_ordering(db, user):
    post1 = Post.objects.create(title='Post 1', slug='post-1', author=user, content='Content 1')
    post2 = Post.objects.create(title='Post 2', slug='post-2', author=user, content='Content 2')
    posts = list(Post.objects.all())
    assert posts[0] == post2
    assert posts[1] == post1
