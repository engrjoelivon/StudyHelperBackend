from django.conf.urls import patterns,url
from basic import views
from basic import updater,mobile




urlpatterns=patterns('',url(r'^$',views.home,name="home"),

                     url(r'^documentation/$',views.documentation,name="documentation"),
                     url(r'^addDevive/$',views.signup,name="signup"),
                     url(r'^login/$',views.log_in,name="log_in"),
                     url(r'^insertrecords/$',views.insert_records,name="insert_records"),
                     url(r'^logout/$',views.user_logout,name="user_logout"),
                     url(r'^start/$',views.start,name="start"),
                     url(r'^content/$',views.content_page,name="content_page"),
                     url(r'^titles/(?P<title_name_url>[\w\-]+)/$', views.titlecontent, name='titlecontent'),
                     url(r'^titlelist/(?P<group_name_url>[\w\-]+)/$', views.grouplink, name='grouplink'),
                     url(r'^updatetitle/$',updater.addTitle,name="addTitle"),
                     url(r'^addMobileTitle/$',mobile.addMobileTitle,name="addMobileTitle"),
                     url(r'^adddevice/$',views.add_device,name="add_device"),
                     url(r'^deleteRecord/$',views.deleteRecord,name="deleteRecord"),
                     url(r'^deleteatstart/$',views.deleteRecord_atstartup,name="deleteRecord_atstartup"),
                     url(r'^removedeletedkeys/$',views.remove_deleted_keys,name="remove_deleted_keys"),

                     url(r'^checkinserts/$',views.check_inserts,name="check_inserts"),
                     url(r'^removeinsertedkey/$',views.remove_inserted_key,name="remove_inserted_key"),
                     url(r'^updaterecords/$',views.update_records,name="update_records"),

                      url(r'^updaterecordwhengiven/$',views.update_record_when_given,name="update_record_when_given"),
                     url(r'^updaterecordsatstartup/$',views.update_records_at_startup,name="update_records_at_startup"),
                    url(r'^removeupdatedkeys/$',views.remove_updated_keys,name="remove_updated_keys"),
                    url(r'^newdevice/$',views.new_device,name="new_device"),








                     )

