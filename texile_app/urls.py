from django.urls import path
from . import views

urlpatterns = [
    path('rmi_chart_data/', views.rmi_chart_data, name="rmi_chart_data"),
    path('rmi_cme_data_push/', views.rmi_cme_data_push, name="rmi_cme_data_push"),
    path('rmi_index_cme/', views.rmi_index_cme, name="rmi_index_cme"),

    path('news_data_updated/', views.news_data_updated, name="news_data_updated"),
    path('default_news_data/', views.default_news_data, name="default_news_data"),
    path('news_data_index/', views.news_data_index, name="news_data_index"),
    # path('data_pull/', views.data_pull, name="data_pull"),
    path('y_data_pull/', views.y_data_pull, name="y_data_pull"),
    path('y_ts_hourly_pull/',views.y_ts_hourly_pull),
    path('y_data_ts_1/<int:duration>', views.y_data_ts_1, name="y_data_ts_1"),
    path('y_data_1/', views.y_data_1, name="y_data_1"),
    path('y_data_2/', views.y_data_2, name="y_data_2"),
    path('y_data_3/', views.y_data_3, name="y_data_3"),
    path('y_data_4/', views.y_data_4, name="y_data_4"),
    path('y_data_5/', views.y_data_5, name="y_data_5"),
    path('y_data_6/', views.y_data_6, name="y_data_6"),
    path('y_stock_data/', views.y_stock_data, name="y_stock_data"),
    path('stock_data_new/', views.stock_data_new, name="stock_data_new"),
    # path('market_cap_data_all/', views.market_cap_data_all, name="market_cap_data_all"),
    # path('market_cap_data_chart/', views.market_cap_data_chart, name="market_cap_data_chart"),
    path('tweet_data_ticker/', views.tweet_data_ticker, name="tweet_data_ticker"),
    path('tweet_data_index/', views.tweet_data_index, name="tweet_data_index"),
    path('tweet_data_landing/', views.tweet_data_landing, name="tweet_data_landing"),
    path('coal_data_pull/', views.coal_data_pull, name="coal_data_pull"),
    path('future_data_pull_CME/', views.future_data_pull_CME, name="future_data_pull_CME"),
    path('f_y_data_1/', views.f_y_data_1, name="f_y_data_1"),
    path('f_y_data_2/', views.f_y_data_2, name="f_y_data_2"),
    path('f_y_data_3/', views.f_y_data_3, name="f_y_data_3"),
    path('f_y_data_4/', views.f_y_data_4, name="f_y_data_4"),
    path('f_y_data_5/', views.f_y_data_5, name="f_y_data_5"),
    path('f_y_data_6/', views.f_y_data_6, name="f_y_data_6"),
    path('pull_index_data/', views.pull_index_data, name="pull_index_data"),
    # path('pull_index_data_rmi/', views.pull_index_data_rmi, name="pull_index_data_rmi"),
    path('index_data_1/', views.index_data_1, name="index_data_1"),
    path('index_data_2/', views.index_data_2, name="index_data_2"),
    path('index_data_3/', views.index_data_3, name="index_data_3"),
    path('index_data_4/', views.index_data_4, name="index_data_4"),
    path('index_data_5/', views.index_data_5, name="index_data_5"),
    path('index_data_6/', views.index_data_6, name="index_data_6"),
    path('pull_latest_data/', views.pull_latest_data, name="pull_latest_data"),
    path('news_image_fetch/', views.news_image_fetch, name="news_image_fetch"),
    path('twitter_data_fetch/', views.twitter_data_fetch, name="twitter_data_fetch"),
    path('version/', views.version, name="version"),
    path('version_check/', views.version_check, name="version_check"),
    path('pull_index_data_hourly/', views.pull_index_data_hourly, name="pull_index_data_hourly"),
    path('send_mail/', views.send_mail, name="send_mail"),
    path('up_time/', views.up_time, name="up_time"),
    path('transport_data_pull/', views.transport_data_pull, name="transport_data_pull"),
    path('baltic_data_pull/', views.baltic_data_pull, name="baltic_data_pull"),
    path('usld_data/', views.usld_data, name="usld_data"),
    path('transport_chart_data/', views.transport_chart_data, name="transport_chart_data"),
    path('transport_index_chart_data/', views.transport_index_chart_data, name="transport_index_chart_data"),
    path('twitter_data_fetch_test/', views.twitter_data_fetch_test, name="twitter_data_fetch_test"),
    path('push_coal/', views.push_coal, name="push_coal"),
    path('future_data_push/', views.future_data_push, name="future_data_push"),
    path('update_chart_count/', views.update_chart_count, name="update_chart_count"),
    path('app_ended/', views.app_ended, name="app_ended"),
    path('page_count/', views.page_count, name="page_count"),
    path('carbon_offset_calc/', views.carbon_offset_calc, name="carbon_offset_calc"),
    path('t_index_data/', views.t_index_data, name="t_index_data"),
    path('customer/', views.customer, name="customer"),
    path('check_terms/', views.check_terms, name="check_terms"),
    path('remove_terms/', views.remove_terms, name="remove_terms"),
    path('add_watchlist/', views.add_watchlist, name="add_watchlist"),
    path('watchlist_config/', views.watchlist_config, name="watchlist_config"),
    path('update_watchlist/', views.update_watchlist, name="update_watchlist"),
    path('feedback_data/', views.feedback_data, name="feedback_data"),
    path('check_feedback/', views.check_feedback, name="check_feedback"),
    path('message/', views.message, name="message"),
    
    path('news_remove_parameter/', views.news_remove_parameter, name="news_remove_parameter"),

    path('rec_news_lp/', views.rec_news_lp, name="rec_news_lp"),
    path('rec_news_tabs/', views.rec_news_tabs, name="rec_news_tabs"),
    path('insert_rec_news/', views.insert_rec_news, name="insert_rec_news"),
    path('expire_news/', views.expire_news, name="expire_news"),
    
    path('fetch_rig_data/', views.fetch_rig_data, name="fetch_rig_data"),
    path('rig_data_1/', views.rig_data_1, name="rig_data_1"),
    path('rig_data_2/', views.rig_data_2, name="rig_data_2"),
    path('rig_data_3/', views.rig_data_3, name="rig_data_3"),
    path('rig_data_4/', views.rig_data_4, name="rig_data_4"),
    path('rig_data_5/', views.rig_data_5, name="rig_data_5"),
    path('rig_data_6/', views.rig_data_6, name="rig_data_6"),

    
    path('fetch_duc_data/', views.fetch_duc_data, name="fetch_duc_data"),
    path('duc_data_1/', views.duc_data_1, name="duc_data_1"),
    path('duc_data_2/', views.duc_data_2, name="duc_data_2"),
    path('duc_data_3/', views.duc_data_3, name="duc_data_3"),
    path('duc_data_4/', views.duc_data_4, name="duc_data_4"),
    path('duc_data_5/', views.duc_data_5, name="duc_data_5"),
    path('duc_data_6/', views.duc_data_6, name="duc_data_6"),


    # website apis
    path('web_data/', views.web_data, name="web_data"),
    path('web_data_df/', views.web_data_df, name="web_data_df"),
    path('send_download_link/', views.send_download_link, name="send_download_link"),
    path('get_config/', views.get_config, name="get_config"),
    path('get_emailID/', views.get_emailID, name="get_emailID"),
    path('add_emailID/', views.add_emailID, name="add_emailID"),
]