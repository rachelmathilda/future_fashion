from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, show_html, register, login_user, logout_user, edit_item, delete_item, add_amount, reduce_amount, get_item_json, create_ajax, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('html/', show_html, name='show_html'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('edit-item/<int:id>/', edit_item, name='edit_item'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'), 
    path('add_amount/<int:id>/', add_amount, name='add_amount'),
    path('reduce_amount/<int:id>/', reduce_amount, name='reduce_amount'), 
    path('get_item_json', get_item_json, name='get_item_json'), 
    path('create_ajax', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]