from django.urls import path
from .views import UploadSongView, AnalysisResultView

urlpatterns = [
    path('upload/', UploadSongView.as_view(), name='upload_song'),
    path('results/<int:song_id>/', AnalysisResultView.as_view(), name='analysis_results'),
]
