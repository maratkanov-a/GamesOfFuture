from django.conf.urls import url
from shop.views import *


urlpatterns = [
    # url(r'^/', ''),

    url(r'^$', HomePage.as_view(), name='home-page'),
    url(r'^category/$', CategoryPage.as_view(), name='category-page'),
    url(r'^products/(?P<pk>\d+)$', ProductsWithCategoryPage.as_view(), name='products-with-category-page'),
    # url(r'^hot/', QuestionListViewHot.as_view(), name='hot-page'),
    # authentication
    # url(r'^login/', 'django.contrib.auth.views.login', name='login-page'),
    # url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout-page'),

    # question pages
    # url(r'^question/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question-page'),
    # url(r'^question/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='question-update-page'),
    # url(r'^questions/$', QuestionListView.as_view(), name='question-list-page'),
    # url(r'^questions/page(?P<page>[0-9]+)/$', QuestionListView.as_view(), name='question-paginate-page'),
    # url(r'^question/create/$', QuestionCreateView.as_view(), name='question-create-page'),
    # url(r'^question/(?P<pk>\d+)/delete/$', QuestionDeleteView.as_view(), name='question-delete-page'),
]
