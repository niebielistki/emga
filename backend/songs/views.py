from rest_framework import generics
from .models import Song, AnalysisResult
from .serializers import SongSerializer, AnalysisResultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UploadSongView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    # Add ML model here

    # def perform_create(self, serializer):
        # song = serializer.save()
        # model_path = os.path.join(os.path.dirname(__file__), 'ml_model/nazwamodelu.joblib')
        # model = joblib.load(model_path)

        # Replace this with your actual model prediction code
        # result = model.predict([song.file.path])

        # Save the analysis result
        # AnalysisResult.objects.create(song=song, result=result)


class AnalysisResultView(APIView):
    def get(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        analysis_result = get_object_or_404(AnalysisResult, song=song)
        serializer = AnalysisResultSerializer(analysis_result)
        return Response(serializer.data)
